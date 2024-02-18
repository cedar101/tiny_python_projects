#!/usr/bin/env python3
"""
usage: hello07_get_args.py [-h] [-n NAME]

Say hello

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name to greet [default: World]
"""

# import argparse

from docopt import docopt
from box import Box


def get_args():
    return Box(docopt(__doc__))
    # parser = argparse.ArgumentParser(description='Say hello')
    # parser.add_argument('-n', '--name', metavar='name',
    #                     default='World', help='Name to greet')
    # return parser.parse_args()


def main():
    args = get_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
