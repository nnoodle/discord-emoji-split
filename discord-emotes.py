#!/usr/bin/env python3
import os
import argparse
from numbers import Number
from wand.display import display
from wand.image import Image


parser = argparse.ArgumentParser(
    description='Split an image into multiple images to use as emotes for Discord®.')
parser.add_argument('input', help='The input image.')
parser.add_argument(
    '-o', '--output', help='The output directory.', default='emotes')
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
    s = args.width * args.height >= 28
    a = round(img.width/args.width*1/33)
    b = -a
    c = None if s else round(img.height/args.height*1.5/33.5)
    d = None if s else -c
    f = img.width/args.width
    g = img.height/args.height
    p = 0
    for j in range(1, args.height + 1):
        with img[:, round((j - 1) * g):round(j * g)] as hcrop:
            for i in range(1, args.width + 1):
                with hcrop[round((i - 1) * f):round(i * f), :] as wcrop:
                    with wcrop[a:b, c:d] as crop:
                        p += 1
                        crop.save(filename=''.join(
                            [args.output, '/', name, str(p), ext]))
                        print(':{0}{1}:'.format(name, p), end='')
            print('')

# with Image(filename=args.input) as img:
#     s = args.width * args.height >= 28
#     a = round(img.width/args.width*1/33)
#     b = -a
#     c = None if s else round(img.height/args.height*1.5/33.5)
#     d = None if s else -c
#     f = img.width/args.width
#     g = img.height/args.height
#     p = 0
#     for j in range(1, args.height + 1):
#         for i in range(1, args.width + 1):
#             with img[round((i - 1) * f)+a:round(i * f)+b, round((j - 1) * g)+c:round(j * g)+d] as crop:
#                 p += 1
#                 crop.save(filename=''.join(
#                     [args.output, '/', name, str(p), ext]))
#                 print(':{0}{1}:'.format(name, p), end='')
#         print('')
