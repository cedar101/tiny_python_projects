#!/usr/bin/env python3
"""
usage: {} [-h] [-v vowel] <text>

Apples and bananas

positional arguments:
  <text>                  Input text or file

options:
  -h, --help            show this help message and exit
  -v vowel, --vowel vowel
                        The vowel to substitute [choices: a e i o u] [default: a]
"""

from pathlib import Path

from box import Box
from type_docopt import docopt, DocoptExit


def replace_vowels(text: str, vowel: str = "a") -> str:
    def new_char(c):
        return vowel if c in "aeiou" else vowel.upper() if c in "AEIOU" else c

    return "".join(new_char(c) for c in text)


# --------------------------------------------------
def get_args():
    docstring = __doc__.format(Path(__file__).name)
    try:
        args = Box(docopt(docstring))
    except ValueError as e:
        strerr = str(e)
        print(f"error: invalid choice: {strerr}" if "is not in" in strerr else strerr)
        raise DocoptExit from e

    p = Path(args.text_)
    if p.is_file():
        args.text_ = p.read_text()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text_
    vowel = args.vowel

    print(replace_vowels(text, vowel))


# --------------------------------------------------
if __name__ == "__main__":
    main()
