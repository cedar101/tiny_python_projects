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
from pathlib import Path

from box import Box
from type_docopt import docopt


def get_args():
    """Get command-line arguments"""
    args = Box(docopt(__doc__.format(Path(__file__).name), types={"path": Path}))
    p = Path(args.text_)
    if p.is_file():
        args.text_ = p.read_text()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    upper_text = args.text_.upper()
    if args.outfile:
        args.outfile.write_text(upper_text, newline="\n")
    else:
        print(upper_text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
