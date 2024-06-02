#!/usr/bin/env python3
"""
usage: {} [-h] [<file>...]

Emulate wc (word count)

positional arguments:
  <file>        Input file(s) [default: sys.stdin]

options:
  -h, --help  show this help message and exit
"""
from typing import Any
import sys
from pathlib import Path

from box import Box
from docopt import docopt

from wc import wc_per_file, print_per_file


# --------------------------------------------------
def get_args() -> dict[str, Any]:
    """Get command-line arguments"""
    args = Box(docopt(__doc__.format(Path(__file__).name)))
    return args


def iter_file(filename, **kwargs):
    with Path(filename).open(**kwargs) as f:
        yield from f


# --------------------------------------------------
def main() -> None:
    args = get_args()
    filenames = args.file_

    files = (
        [(iter_file(fname), fname) for fname in filenames]
        if filenames
        else [(sys.stdin, "<stdin>")]
    )
    total_lines, total_words, total_bytes = 0, 0, 0
    for file, name in files:
        num_lines, num_words, num_chars = wc_per_file(file)
        print_per_file(num_lines, num_words, num_chars, name)
        total_lines += num_lines
        total_bytes += num_chars
        total_words += num_words

    if len(files) > 1:
        print_per_file(total_lines, total_words, total_bytes, "total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
