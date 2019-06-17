"""Generates code snippets.

Usage:
    $ python factory/codesnippets.py

"""
import os

from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter
import weasyprint

from sublette import Sublette

HERE = os.path.dirname(__file__)
OUTPUT_PATTERN = os.path.join(HERE, '../showcase/%s.png')
INPUT_DIR = os.path.join(HERE, 'codesnippets')
TEMPLATE = '''
<html>
<head>
  <style>
    @import url(https://fonts.googleapis.com/css?family=Roboto+Mono);
    @page {
      size: %(width)dpx %(height)dpx;
      margin: 0;
      padding: 0;
    }
    body {
      margin: 0;
      padding: 10px 30px;
    }
    pre {
      font-family: "Roboto Mono", monospace;
      font-size: 16px;
      line-height: 20px;
      tab-size: 4;
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

    lexer = get_lexer_for_filename(filename)
    lexer.add_filter(Sublette.filter())
    highlighted = highlight(code, lexer, formatter)

    lines = code.split('\n')
    columns = max(len(line) for line in lines)
    rows = len(lines)

    html = weasyprint.HTML(string=TEMPLATE % {
        'css': formatter.get_style_defs('body'),
        'html': highlighted,
        'width': (columns+6) * 10,
        'height': (rows+2) * 20,
    })

    output_path = OUTPUT_PATTERN % filename
    with open(output_path, 'wb') as f:
        html.write_png(f, font_config=font_config)

    print(os.path.relpath(output_path, os.path.curdir))
