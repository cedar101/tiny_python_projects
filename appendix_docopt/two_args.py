#!/usr/bin/env python3
"""
usage: two_args.py [-h] <color> <size>

Two positional arguments

positional arguments:
  <color>       The color of the garment
  <size>        The size of the garment

options:
  -h, --help  show this help message and exit
"""

from docopt import docopt
from box import Box


# --------------------------------------------------
def get_args():
    # TODO: use Pydantic
    return Box(docopt(__doc__))


# --------------------------------------------------
def main():
    args = get_args()
    print("color =", args.color_)
    print("size =", args.size_)


# --------------------------------------------------
if __name__ == "__main__":
    main()
