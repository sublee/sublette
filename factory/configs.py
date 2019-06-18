"""Generates editor configurations.

Usage:
    $ python factory/configs.py

"""
from pathlib import Path

from sublette import sublette


vars = {}
for name, color in sublette.items():
    if len(color) == 4:
        r = int(color[1]*2, base=16)
        g = int(color[2]*2, base=16)
        b = int(color[3]*2, base=16)
    else:
        r = int(color[1:3], base=16)
        g = int(color[3:5], base=16)
        b = int(color[5:7], base=16)

    # %(Color)s = #0b1621
    vars[name] = color

    # %(rgb[Color])s = 11,22,33
    # %(r[Color])s = 11
    # %(g[Color])s = 22
    # %(b[Color])s = 33
    vars['rgb[%s]' % name] = '%d,%d,%d' % (r, g, b)
    vars['r[%s]' % name] = r
    vars['g[%s]' % name] = g
    vars['b[%s]' % name] = b

    # %(rf[Color])s = 0.0431372549019608
    # %(gf[Color])s = 0.0862745098039216
    # %(bf[Color])s = 0.0862745098039216
    vars['rf[%s]' % name] = r/255
    vars['gf[%s]' % name] = g/255
    vars['bf[%s]' % name] = b/255


# Generate configurations.
here = Path(__file__).parent
for filename in here.glob('configs/**/*'):
    if filename.is_dir():
        continue
    if filename.name.startswith('.'):
        continue

    with open(filename) as f:
        template = f.read()

    rendered = template % vars

    output_path = here.parent/filename.relative_to(here)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open('w') as f:
        f.write(rendered)

    print(output_path)
