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
from contextlib import ExitStack

from box import Box
from docopt import docopt

from wc import wc_1file


# --------------------------------------------------
def get_args() -> dict[str, Any]:
    """Get command-line arguments"""
    args = Box(docopt(__doc__.format(Path(__file__).name)))
    return args


def print_wc(num_lines: int, num_words: int, num_chars: int, filename: str) -> None:
    print(f"{num_lines:8}{num_words:8}{num_chars:8} {filename}")


# --------------------------------------------------
def main() -> None:
    args = get_args()
    filenames = args.file_

    with ExitStack() as stack:
        files = (
            [stack.enter_context(Path(fname).open()) for fname in filenames]
            if filenames
            else [sys.stdin]
        )
        total_lines, total_words, total_chars = 0, 0, 0
        for f in files:
            num_lines, num_words, num_chars = wc_1file(f)
            print_wc(num_lines, num_words, num_chars, f.name)
            total_lines += num_lines
            total_chars += num_chars
            total_words += num_words

    if len(files) > 1:
        print_wc(total_lines, total_words, total_chars, "total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
