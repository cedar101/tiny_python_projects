#!/usr/bin/env python3
"""
usage: solution2_list.py [-h] [-s SEED] [-m MUTATIONS] <text>

Telephone

positional arguments:
  <text>                  Input text or file

options:
  -h, --help            show this help message and exit
  -s SEED, --seed=SEED  Random seed [type: int]
  -m MUTATIONS, --mutations=MUTATIONS
                        Percent mutations [type: float] [default: 0.1]
"""

from pathlib import Path
import random
import string

from type_docopt import docopt, DocoptExit
from box import Box


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    docstring = __doc__.format(Path(__file__).name)
    try:
        args = Box(docopt(docstring))
    except ValueError as e:
        strerr = str(e)
        if "invalid literal for int() with base 10" in strerr:
            _0, _1, invalid_literal = strerr.rpartition(" ")
            strerr = f"invalid int value: {invalid_literal}"
        elif "could not convert string to float" in strerr:
            _0, _1, invalid_literal = strerr.rpartition(" ")
            strerr = f"invalid float value: {invalid_literal}"
        raise DocoptExit(f"error: {strerr}") from e

    if not 0 <= args.mutations <= 1:
        raise DocoptExit(f'--mutations "{args.mutations}" must be between 0 and 1')

    p = Path(args.text_)
    if p.is_file():
        args.text_ = p.read_text()

    return args


def mutate_text(text, mutations: float = 0.1, seed: int = None) -> str:
    def exclude_same(i: int):
        return alpha.replace(text_list[i], "")

    random.seed(seed)
    alpha = f"{string.digits}{string.ascii_letters}{string.punctuation}"
    len_text = len(text)
    num_mutations = round(mutations * len_text)
    text_list = list(text)

    for i in random.sample(range(len_text), num_mutations):
        text_list[i] = random.choice(exclude_same(i))
    return "".join(text_list)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text_
    new_text = mutate_text(text, args.mutations, args.seed)
    print(f'You said: "{text}"\nI heard : "{new_text}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
