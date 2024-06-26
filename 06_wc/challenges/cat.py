#!/usr/bin/env python3
"""
usage: cat.py [options] <file>

Python version of `cat`, manually checking and opening file argument

positional arguments:
  file          Input file [type: path]

options:
  -h, --help    show this help message and exit
  -n, --number  number all output lines  
"""

from pathlib import Path

from docopt import docopt, DocoptExit
from box import Box


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    args = Box(docopt(__doc__))
    args.file = Path(args.file_)
    if not args.file.is_file():
        raise DocoptExit(f'"{args.file}" is not a file')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    with args.file.open() as f:
        if args.number:
            for i, line in enumerate(f, start=1):
                print(f"{i:6}  {line}", end="")
        else:
            for line in f:
                print(line, end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
