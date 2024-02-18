#!/usr/bin/env python3
"""
usage: two_args.py [-h] <color> <size>

Two positional arguments

positional arguments:
  <color>       The color of the garment
  <size>        The size of the garment [type: int]

options:
  -h, --help  show this help message and exit
"""

import sys

from docopt import docopt, DocoptExit
from pydantic import ConfigDict, AliasGenerator, ValidationError
from pydantic.dataclasses import dataclass


TRACEBACK_LIMIT = 1000


@dataclass(
    config=ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field_name: f"<{field_name}>"
        )
    )
)
class GarmentArguments:
    color: str
    size: int


# --------------------------------------------------
def get_args():
    try:
        return GarmentArguments(**docopt(__doc__))
    except ValidationError as e:
        raise DocoptExit(str(e)) from e


# --------------------------------------------------
def main():
    args = get_args()
    print("color =", args.color)
    print("size =", args.size)


# --------------------------------------------------
if __name__ == "__main__":
    main()
