#!/usr/bin/env python3
"""
usage: {} [-h] [-o FILE] <text>

Howler (upper-cases input)

positional arguments:
  <text>                    Input string or file

options:
  -h, --help                Show this help message and exit
  -o FILE, --outfile FILE   Output filename [type: path]
"""
import io
import sys
from pathlib import Path

from box import Box
from type_docopt import docopt


def get_args():
    """Get command-line arguments"""
    args = Box(docopt(__doc__.format(Path(__file__).name), types={"path": Path}))
    p = Path(args.text_)
    if p.is_file():
        args.text_ = p
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text_
    outfile = args.outfile
    with (
        io.StringIO(text) if isinstance(text, str) else text.open() as infile,
        outfile.open("w") if outfile else sys.stdout as outfile,
    ):
        for line in infile:
            outfile.write(line.upper())


# --------------------------------------------------
if __name__ == "__main__":
    main()
