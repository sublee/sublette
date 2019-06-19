"""A Pygments lexer and style injector for ANSI display attributes."""
from itertools import product
from typing import Dict, Optional, Set

from pygments.filters import TokenMergeFilter
from pygments.lexer import RegexLexer
from pygments.token import Token


def get_token(effects: Set[int],
              fg: Optional[int],
              bg: Optional[int],
              ) -> type(Token):
    """Gets a Pygments token for the given ANSI display attributes."""
    union = effects.union([fg, bg])
    union.discard(None)

    if not union:
        return Token.ANSI

    # Example: Token.ANSI.SGR_1_4_7_30
    token_name = 'SGR_' + '_'.join(str(x) for x in sorted(union))
    token = getattr(Token.ANSI, token_name)
    return token


class ANSILexer(RegexLexer):
    name = 'ansi'
    aliases = []
    filenames = ['*.ansi']

    tokens = {
        'root': [
            (r'(\033|\x1B)\[[^m]*m', Token.ANSI.Escape),
        ]
    }

    def __init__(self):
        super().__init__()
        self.add_filter(TokenMergeFilter())

    def apply_esc(self, seq, effects, fg, bg):
        """Returns ANSI display attributes updated by the given escape
        sequence.
        """
        effects = set(effects)

        assert seq.endswith('m')
        _, _, effectsat_code = seq[:-1].partition('[')
        for code in effectsat_code.split(';'):
            if not code:
                continue

            code = int(code)
            cat = code//10

            # Reset all attributes.
            if code == 0:
                effects.clear()
                fg = bg = None

            # Reset specific flag.
            elif cat == 2:
                effects.discard(code % 10)

            # Add a flag.
            elif cat == 0:
                effects.add(code)

            # Set foreground color.
            elif cat in [3, 9]:
                fg = code

            # Set background color.
            elif cat in [4, 10]:
                bg = code

        return effects, fg, bg

    def get_tokens_unprocessed(self, text):
        tokens = RegexLexer.get_tokens_unprocessed(self, text)

        effects, fg, bg = set(), None, None

        for index, token, value in tokens:
            if token is Token.ANSI.Escape:
                effects, fg, bg = self.apply_esc(value, effects, fg, bg)
                continue

            yield index, get_token(effects, fg, bg), value


def sequences():
    """Generates supporting ANSI display attributes."""
    color_codes = [
        None,
        30, 31, 32, 33, 34, 35, 36, 37,
        90, 91, 92, 93, 94, 95, 96, 97,
    ]

    # Supported effects:
    #   1 = Bold
    #   4 = Underline
    #   7 = Reverse
    for effects in product([None, 1], [None, 4], [None, 7]):
        effects = set(filter(bool, effects))

        for fg, bg in product(color_codes, color_codes):
            if bg is not None:
                bg += 10

            yield effects, fg, bg


def inject(styles: Dict[type(Token), str], palette: Dict[str, str]):
    """Injects styles for ANSI display attributes."""
    color_names = [
        'Black', 'Red', 'Green', 'Yellow',
        'Blue', 'Magenta', 'Cyan', 'White',
    ]
    bright_color_names = [
        'Bright Black', 'Bright Red', 'Bright Green', 'Bright Yellow',
        'Bright Blue', 'Bright Magenta', 'Bright Cyan', 'Bright White',
    ]

    styles[Token.ANSI] = palette['Foreground']

    for effects, fg, bg in sequences():
        token = get_token(effects, fg, bg)

        style = []

        # 1 = Bold
        if 1 in effects:
            if fg is not None and 30 <= fg < 40:
                fg += 60

        # 4 = Underline
        if 4 in effects:
            style.append('underline')

        # 7 = Reverse
        if 7 in effects:
            fg, bg = bg, fg

        # 30-39 = Foreground Color
        # 90-99 = Foreground Bright Color
        if fg is not None:
            if 30 <= fg < 40:
                style.append(palette[color_names[fg % 10]])
            else:
                style.append(palette[bright_color_names[fg % 10]])

        # 40-49 = Background Color
        # 100-109 = Background Bright Color
        if bg is not None:
            style.append('bg:%s' % palette[color_names[bg % 10]])

        styles[token] = ' '.join(style)
