"""Generates color plates.

Usage:
    $ python factory/plates.py

"""
import os

from PIL import Image

from sublette import sublette

HERE = os.path.dirname(__file__)
OUTPUT_PATTERN = os.path.join(HERE, '../plates/%s.gif')

for name, color in sublette.items():
    output = OUTPUT_PATTERN % name.lower().replace(' ', '-')
    img = Image.new('RGB', (18, 18), color)
    img.convert('P')
    img.save(output)
