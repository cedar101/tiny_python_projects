#!/usr/bin/env python3
"""
usage: one_arg.py [-h] <name>

A single positional argument

positional arguments:
  <name>        The name to greet

options:
  -h, --help  show this help message and exit
"""

from docopt import docopt
from box import Box


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    return Box(docopt(__doc__))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(f"Hello, {args.name_}!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
