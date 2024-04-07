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
import io
import sys
from pathlib import Path

from box import Box
from docopt import docopt


# --------------------------------------------------
def get_args() -> dict[str, Any]:
    """Get command-line arguments"""
    args = Box(docopt(__doc__.format(Path(__file__).name)))
    return args


def wc_1file(f: io.TextIOBase) -> tuple[int, int, int]:
    num_lines, num_words, num_chars = 0, 0, 0
    for line in f:
        num_lines += 1
        num_words += len(line.split())
        num_chars += len(line)
    return num_lines, num_words, num_chars


def print_wc(num_lines: int, num_words: int, num_chars: int, filename: str) -> None:
    print(f"{num_lines:8}{num_words:8}{num_chars:8} {filename}")


# --------------------------------------------------
def main() -> None:
    args = get_args()

    if args.file_:
        total_lines, total_words, total_chars = 0, 0, 0
        for fp in args.file_:
            with Path(fp).open() as f:
                num_lines, num_words, num_chars = wc_1file(f)
            print_wc(num_lines, num_words, num_chars, fp)
            total_lines += num_lines
            total_chars += num_chars
            total_words += num_words
    else:
        total_lines, total_words, total_chars = wc_1file(sys.stdin)

    print_wc(total_lines, total_words, total_chars, "total" if args.file_ else "")


# --------------------------------------------------
if __name__ == "__main__":
    main()
