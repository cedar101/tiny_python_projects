#!/usr/bin/env python3
"""
usage: {} [-h] [-s SEED] <text>

Ransom Note

positional arguments:
  <text>                Input text or file

options:
  -h, --help            show this help message and exit
  -s SEED, --seed=SEED  Random seed [type: int]
"""
from pathlib import Path
import random
from type_docopt import docopt, DocoptExit
from box import Box


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    docstring = __doc__.format(Path(__file__).name)
    try:
        args = Box(docopt(docstring))
    except ValueError as e:
        raise DocoptExit(f"error: {e}") from e

    p = Path(args.text_)
    if p.is_file():
        args.text_ = p.read_text()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    # Method 3: Iterate each character, add to a str
    ransom = ""
    for char in args.text_:
        ransom += choose(char)

    print("".join(ransom))


# --------------------------------------------------
def choose(char):
    """Randomly choose an upper or lowercase letter to return"""

    return random.choice((char.lower, char.upper))()


# --------------------------------------------------
if __name__ == "__main__":
    main()
