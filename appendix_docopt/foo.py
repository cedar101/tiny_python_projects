#!/usr/bin/env python
"""
usage: foo.py [-h] [-a STR] [-i INT] [-f FILE] [-o] <positional>

Rock the Casbah

positional arguments:
  <positional>                   A positional argument

options:
  -h, --help            show this help message and exit
  -a STR, --arg STR     A named string argument [default: ''] [type: str]
  -i INT, --int INT     A named integer argument [default: 0] [type: int]
  -f FILE, --file FILE  A readable file [default: None] [type: path]
  -o, --on              A boolean flag [default: False]
"""
from pathlib import Path

from type_docopt import docopt
from box import Box


def get_args():
    """Get command-line arguments"""
    return Box(docopt(__doc__, types={"path": Path}))


def main():
    args = get_args()
    """Make a jazz noise here"""

    args = get_args()
    print(args)
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional_

    print(f"str_arg = {str_arg!r}")
    print(f"int_arg = {int_arg}")
    print(f"file_arg = {file_arg.name if file_arg else ''!r}")
    print(f"flag_arg = {flag_arg}")
    print(f"positional = {pos_arg!r}")


if __name__ == "__main__":
    main()
