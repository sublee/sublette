"""Generates kitsch.

Usage:
    $ python factory/kitsch.py

A kitsch is designed with a PSD format. This script renders PSD files with the
theme colors. Layer names indicate which color should be picked. If a layer
isn't named with a color name, it will be used as it stands.

"""
import os

from PIL import Image
from psd_tools import PSDImage

from sublette import sublette

HERE = os.path.dirname(__file__)
OUTPUT_PATTERN = os.path.join(HERE, '../showcase/%s.png')
INPUT_DIR = os.path.join(HERE, 'kitsch')

for filename in os.listdir(INPUT_DIR):
    if filename.startswith('.'):
        continue
    elif not filename.endswith('.psd'):
        continue

    psd_path = os.path.join(INPUT_DIR, filename)
    psd = PSDImage.open(psd_path)

    img = Image.new('RGBA', psd.size)

    for layer in psd:
        if not layer.visible:
            continue

        framed = Image.new('RGBA', psd.size)
        framed.paste(layer.compose(), layer.offset)

        try:
            # Choose a theme color by layer name. (case sensitive)
            color = sublette[layer.name]
        except KeyError:
            # Paste as it stands.
            img.paste(framed, (0, 0), framed)
        else:
            # Fill with the theme color.
            alpha = framed
            img.paste(Image.new('RGB', psd.size, color), (0, 0), alpha)

    output_path = OUTPUT_PATTERN % filename.rpartition('.psd')[0]
    img.save(output_path)

    print(os.path.relpath(output_path, os.path.curdir))
