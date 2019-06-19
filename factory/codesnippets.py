"""Generates code snippets.

Usage:
    $ python factory/codesnippets.py

"""
import os

import weasyprint
from pygments import highlight
from pygments.formatters import HtmlFormatter, NullFormatter
from pygments.lexers import get_lexer_for_filename

from ansi import ANSILexer
from sublette import Sublette

HERE = os.path.dirname(__file__)
OUTPUT_PATTERN = os.path.join(HERE, '../showcase/%s.png')
INPUT_DIR = os.path.join(HERE, 'codesnippets')
TEMPLATE = '''
<html>
<head>
  <style>
    @import url(https://fonts.googleapis.com/css?family=Roboto+Mono:500);
    @page {
      size: %(width)dpx %(height)dpx;
      margin: 0;
      padding: 0;
    }
    body {
      margin: 0;
      padding: 15px 45px;
    }
    pre {
      font-family: "Roboto Mono", monospace;
      font-weight: 500;
      font-size: 24px;
      line-height: 30px;
      tab-size: 4;
    }
    pre span {
        display: inline-block;
    }
  </style>
  <style>%(css)s</style>
</head>
<body>
  %(html)s
</body>
</html>
'''


formatter = HtmlFormatter(style=Sublette)
font_config = weasyprint.fonts.FontConfiguration()

for filename in os.listdir(INPUT_DIR):
    if filename.startswith('.'):
        continue

    with open(os.path.join(INPUT_DIR, filename), encoding='utf-8') as f:
        code = f.read()

    if filename.endswith('.ansi'):
        lexer = ANSILexer()
    else:
        lexer = get_lexer_for_filename(filename)
    lexer.add_filter(Sublette.filter())
    highlighted = highlight(code, lexer, formatter)

    # Detect size by output instead of input.
    text = highlight(code, lexer, NullFormatter())
    lines = text.split('\n')
    columns = max(len(line.rstrip()) for line in lines)
    rows = len(lines)

    html = weasyprint.HTML(string=TEMPLATE % {
        'css': formatter.get_style_defs('body'),
        'html': highlighted,
        'width': (columns+4) * 15,
        'height': (rows+2) * 30,
    })

    output_path = OUTPUT_PATTERN % filename
    with open(output_path, 'wb') as f:
        html.write_png(f, font_config=font_config)
    print(os.path.relpath(output_path, os.path.curdir))
