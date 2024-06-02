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

from box import Box
from docopt import docopt

from wc import wc_per_file, print_per_file


# --------------------------------------------------
def get_args() -> dict[str, Any]:
    """Get command-line arguments"""
    args = Box(docopt(__doc__.format(Path(__file__).name)))
    return args


# --------------------------------------------------
def main() -> None:
    args = get_args()
    filenames = args.file_

    total_words, total_bytes, num_lines, num_words, num_bytes = 0, 0, 0, 0, 0
    # breakpoint()
    if not filenames:
        filenames = ["-"]
    filename = filenames[0]
    for line in fileinput.input(filenames):
        if fileinput.isfirstline() and filename != fileinput.filename():
            total_bytes += num_bytes
            total_words += num_words
            print_per_file(num_lines, num_words, num_bytes, filename)
            num_lines, num_words, num_bytes = 0, 0, 0
            filename = fileinput.filename()

        num_lines = fileinput.filelineno()
        num_words += len(line.split())
        num_bytes += len(line.encode())

    print_per_file(num_lines, num_words, num_bytes, fileinput.filename())
    total_bytes += num_bytes
    total_words += num_words

    if len(filenames) > 1:
        print_per_file(fileinput.lineno(), total_words, total_bytes, "total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
