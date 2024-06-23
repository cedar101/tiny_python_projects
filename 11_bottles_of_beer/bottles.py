#!/usr/bin/env python3
"""
usage: bottles.py [-h] [-r] [-n NUMBER]

Bottles of beer song

options:
  -h, --help                show this help message and exit
  -n NUMBER, --num NUMBER   How many bottles [type: int] [default: 10]
  -r, --reverse
"""
from textwrap import dedent

from type_docopt import docopt, DocoptExit
from box import Box


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    try:
        args = Box(docopt(__doc__))
    except ValueError as e:
        strerr = str(e)
        if "invalid literal for int() with base 10" in strerr:
            _0, _1, invalid_literal = strerr.rpartition(" ")
            strerr = f"invalid int value: {invalid_literal}"
        raise DocoptExit(f"error: {strerr}") from e

    if args.num < 1:
        raise DocoptExit(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print(
        "\n\n".join(
            verse(bottle)
            for bottle in (
                range(1, args.num + 1) if args.reverse else range(args.num, 0, -1)
            )
        )
    )


# --------------------------------------------------
def verse(bottle):
    """Sing a verse"""

    next_bottle = bottle - 1
    s1 = "" if bottle == 1 else "s"
    s2 = "" if next_bottle == 1 else "s"
    num_next = "No more" if next_bottle == 0 else next_bottle
    return dedent(
        f"""\
        {bottle} bottle{s1} of beer on the wall,
        {bottle} bottle{s1} of beer,
        Take one down, pass it around,
        {num_next} bottle{s2} of beer on the wall!"""
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
