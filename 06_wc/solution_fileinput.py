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
import fileinput
import itertools

from box import Box
from docopt import docopt

from wc import wc_per_file, print_per_file


# --------------------------------------------------
def get_args() -> dict[str, Any]:
    """Get command-line arguments"""
    args = Box(docopt(__doc__.format(Path(__file__).name)))
    return args


def open_check_empty(filename, mode="r"):
    p = Path(filename)
    if p.stat().st_size == 0:
        print_per_file(0, 0, 0, filename)
    return p.open(mode)


# --------------------------------------------------
def main() -> None:
    args = get_args()
    filenames = args.file_

    if not filenames:
        filenames = ["-"]

    total_words, total_bytes = 0, 0
    for filename, group in itertools.groupby(
        fileinput.input(filenames, openhook=open_check_empty),
        lambda x: fileinput.filename(),
    ):
        num_lines, num_words, num_bytes = wc_per_file(group)
        print_per_file(num_lines, num_words, num_bytes, filename)
        total_bytes += num_bytes
        total_words += num_words

    if len(filenames) > 1:
        print_per_file(fileinput.lineno(), total_words, total_bytes, "total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
