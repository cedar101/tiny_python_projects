#!/usr/bin/env python3
"""
usage: {} [-h] [-f FILE] [<letter>...]

Gashlycrumb

positional arguments:
  <letter>              Letter(s)

options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Input file [type: path] [default: gashlycrumb.txt]
"""
from typing import Any
from pathlib import Path
from functools import partial

from box import Box
from type_docopt import docopt


# --------------------------------------------------
def get_args() -> dict[str, Any]:
    """Get command-line arguments"""
    args = Box(docopt(__doc__.format(Path(__file__).name), types={"path": Path}))
    return args


# --------------------------------------------------
def main() -> None:
    args = get_args()

    with args.file.open() as f:
        lookup = {line[0].upper(): line.rstrip() for line in f}

    for letter in args.letter_ or iter(
        partial(input, "Please provide a letter [! to quit]: "), "!"
    ):
        print(lookup.get(letter.upper(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == "__main__":
    main()
