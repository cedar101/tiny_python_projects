#!/usr/bin/env python3
"""
usage: manual.py [-h] [-v INT]

Manually check an argument

options:
  -h, --help         show this help message and exit
  -v INT, --val=INT  value between 1 and 10 [default: 5] [type: int]
"""

from type_docopt import docopt, DocoptExit
from box import Box


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    try:
        args = Box(docopt(__doc__))  # <1>
    except ValueError as e:
        raise DocoptExit(str(e)) from e
    if not 1 <= args.val <= 10:  # <2>
        raise DocoptExit(f"--val={args.val} must be between 1 and 10")  # <3>
    return args  # <4>


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(f"val = {args.val}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
