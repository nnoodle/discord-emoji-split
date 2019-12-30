<!-- -*- eval:(auto-fill-mode 1) -*- -->
# discord-emoji-split
A tiny script that splits an image up to use as emojis for Discord.

## Dependencies
This script depends on [Wand](http://docs.wand-py.org).

Install the MagickWand library with your package manager, and `Wand` with `pip`.

```shell
$ apt-get install libmagickwand-dev
$ pip install Wand
```

## Usage
Running `discord-emoji-split.py` with only an image argument will
split that image into a 2×2 to a directory named `emojis`, then
output the emoji codes.

```shell
$ ./discord-emoji-split.py foo.png
:foo1::foo2:
:foo3::foo4:
```

You can also change the width, height, and output directory with the
`-x`, `-y`, and `-o` flags respectively.

```shell
$ ./discord-emoji-split.py foo.png -x 3 -y 4 -o bar
:foo1::foo2::foo3:
:foo4::foo5::foo6:
:foo7::foo8::foo9:
:foo10::foo11::foo12:
```

As a rule of thumb, the width and height should be proportional to the
image.
