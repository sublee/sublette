"""Generates editor configurations.

Usage:
    $ python factory/configs.py

"""
from pathlib import Path

from sublette import sublette


# %(Color)s = #rrggbb or #rgb
# %(rgb[Color])s = 11,22,33
vars = {}
for name, color in sublette.items():
    vars[name] = color

    if len(color) == 4:
        r = int(color[1]*2, base=16)
        g = int(color[2]*2, base=16)
        b = int(color[3]*2, base=16)
    else:
        r = int(color[1:3], base=16)
        g = int(color[3:5], base=16)
        b = int(color[5:7], base=16)

    vars['rgb[%s]' % name] = '%d,%d,%d' % (r, g, b)


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
