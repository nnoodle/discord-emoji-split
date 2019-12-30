#!/usr/bin/env python3
import os
from argparse import ArgumentParser
from re import sub
from fractions import Fraction
from wand.image import Image
# from wand.display import display


parser = ArgumentParser(
    description='Split an image into multiple images to use as emojis for Discord®.')
parser.add_argument('input', help='The input image.')
parser.add_argument(
    '-x', '--width', help='Width of the output.', type=int, default=2)
parser.add_argument(
    '-y', '--height', help='Height of the output.', type=int, default=2)
parser.add_argument(
    '-e', '--ext', help='Filename extension')
parser.add_argument(
    '-o', '--output', help='The output directory.', default='emojis')
args = parser.parse_args()

if not os.path.exists(args.output):
    os.mkdir(args.output)
elif not os.path.isdir(args.output):
    raise OSError('Not a directory', args.output)

name, ext = os.path.splitext(os.path.basename(args.input))
name = sub('[^A-Za-z0-9_]', '', name)
ext = '.'+args.ext if args.ext else ext
args.output = os.path.abspath(args.output)


def resize(img):
    if Fraction(img.width, img.height) == Fraction(args.width, args.height):
        return img.width, img.height

    x = img.width - (img.width % args.width)
    y = x * Fraction(args.height, args.width)
    if y.denominator != 1:
        x = x.denominator*x
        y = y.denominator*y
    y = round(y)

    img.sample(x, y)
    return x, y


with Image(filename=args.input) as img:
    x, y = resize(img)

    f = x/args.width
    g = y/args.height

    count = 0
    for j in range(1, args.height+1):
        for i in range(1, args.width+1):
            with img[round((i-1)*f):round(i*f), round((j-1)*g):round(j*g)] as crop:
                count += 1
                crop.save(filename=''.join(
                    [args.output, '/', name, str(count), ext]))
                print(':{}{}:'.format(name, count), end='')
        print() # newline
