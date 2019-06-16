import io
import os

import lxml.html
from markdown import Markdown
from pygments.filter import simplefilter
from pygments.style import Style
from pygments.token import Token

__all__ = ['sublette', 'Sublette']


def read_sublette():
    """Reads the color table of Sublette from README.md."""
    readme_path = os.path.join(os.path.dirname(__file__), '../README.md')
    with open(readme_path) as f:
        readme = f.read()

    markdown = Markdown(extensions=['markdown.extensions.tables'])
    html = lxml.html.parse(io.StringIO(markdown.convert(readme)))

    colors = {}
    for td_name in html.xpath('//table/tbody//td[1]'):
        td_hex = td_name.getnext()

        name = td_name.text_content()
        hex = td_hex.text_content()

        colors[name] = hex
    return colors


#: The color table of Sublette.
sublette = read_sublette()


class Sublette(Style):
    """A Pygments style for Sublette."""
    background_color = sublette['Background']
    styles = {
        # Actually, "default_style" is not implemented.
        Token: sublette['Foreground'],

        Token.Comment:             sublette['Blue'],
        Token.Keyword:             sublette['Yellow'],
        Token.Keyword.Constant:    sublette['Cyan'],
        Token.Keyword.Namespace:   sublette['Magenta'],
        Token.Name.Builtin:        sublette['Cyan'],
        Token.Name.Builtin.Pseudo: 'noinherit',
        Token.Name.Class:          sublette['Cyan'],
        Token.Name.Function:       sublette['Cyan'],
        Token.Name.Exception:      sublette['Green'],
        Token.Name.Decorator:      sublette['Cyan'],
        Token.Name.Decorator.Sign: sublette['Magenta'],
        Token.Name.Tag:            sublette['Yellow'],
        Token.Name.Attribute:      sublette['Green'],
        Token.Operator.Word:       sublette['Yellow'],
        Token.String:              sublette['Red'],
        Token.Number:              sublette['Red'],
        Token.Text:                sublette['Magenta'],
    }

    @simplefilter
    def filter(self, lexer, stream, options):
        for ttype, value in stream:
            if ttype is Token.Name.Decorator and value.startswith('@'):
                yield Token.Name.Decorator.Sign, '@'
                yield Token.Name.Decorator, value[1:]
                continue
            yield ttype, value
