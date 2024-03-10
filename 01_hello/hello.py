#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark <kyclark@gmail.com>
Purpose: Say hello

Usage: hello.py [-h] [-n NAME]

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name to greet [default: World]
"""

# import argparse
from docopt import docopt
from box import Box


# --------------------------------------------------
def get_args():
    """Get the command-line arguments"""
    return Box(docopt(__doc__))
    # parser = argparse.ArgumentParser(description='Say hello')
    # parser.add_argument('-n', '--name', default='World', help='Name to greet')
    # return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(f"Hello, {args.name}!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
