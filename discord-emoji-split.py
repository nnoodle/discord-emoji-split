#!/usr/bin/env python3
import os
import argparse
from math import ceil
from numbers import Number
from wand.display import display
from wand.image import Image


parser = argparse.ArgumentParser(
    description='Split an image into multiple images to use as emojis for Discord®.')
parser.add_argument('input', help='The input image.')
parser.add_argument(
    '-o', '--output', help='The output directory.', default='emojis')
parser.add_argument(
    '-x', '--width', help='Width of the output.', type=int, default=2)
parser.add_argument(
    '-y', '--height', help='Height of the output.', type=int, default=2)
args = parser.parse_args()

if not os.path.exists(args.output):
    os.mkdir(args.output)
elif not os.path.isdir(args.output):
    raise OSError('Not a directory', args.output)

name, ext = os.path.splitext(os.path.basename(args.input))
args.output = os.path.abspath(args.output)

with Image(filename=args.input) as img:
    f = img.width/args.width
    g = img.height/args.height
    a = f * 1/25 # (2/66 + 3/83 + 4/100 + 4/116)/4
    b = 0 if args.width * args.height >= 28 else g * \
        1/25 # (3/67 + 4/84 + 5/101 + 5/117)/4
    p = 0
    for j in range(1, args.height + 1):
        for i in range(1, args.width + 1):
            with img[ceil((i - 1) * f + a):ceil(i * f - a), ceil((j - 1) * g + b):ceil(j * g - b)] as crop:
                p += 1
                crop.save(filename=''.join(
                    [args.output, '/', name, str(p), ext]))
                print(':{0}{1}:'.format(name, p), end='')
        print('')
