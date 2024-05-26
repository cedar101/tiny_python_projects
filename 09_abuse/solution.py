#!/usr/bin/env python3
"""
usage: solution.py [-h] [-a ADJECTIVES] [-n INSULTS] [-s SEED]

Heap abuse

options:
    -h, --help                              show this help message and exit
    -a ADJECTIVES, --adjectives=ADJECTIVES  Number of adjectives [default: 2] [type: int]
    -n INSULTS, --number=INSULTS            Number of insults [default: 3] [type: int]
    -s SEED, --seed=SEED                    Random seed [type: int]
"""

from box import Box
from type_docopt import docopt, DocoptExit

from abuse import insult


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

    if args.adjectives < 1:
        raise DocoptExit(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        raise DocoptExit(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print("\n".join(insult(args.adjectives, args.number, args.seed)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
