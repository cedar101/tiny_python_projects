#!/usr/bin/env python3
"""
usage: choices.py [-h] <color> <size>

(Choices are deliminated by space.)

positional arguments:
  <color>       Color [choices: {color_choices}]
  <size>        The size of the garment [type:int] [choices: {size_choices}]

options:
  -h, --help  show this help message and exit
"""

import typing

from docopt import docopt, DocoptExit
from pydantic import Field, ConfigDict, AliasGenerator, ValidationError
from pydantic.dataclasses import dataclass


TRACEBACK_LIMIT = 1000
COLOR_LITERALS = typing.Literal["red", "yellow", "blue"]
SIZE_CHOICES = tuple(range(1, 11))


@dataclass(
    config=ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field_name: f"<{field_name}>"
        )
    )
)
class GarmentArguments:
    color: COLOR_LITERALS
    size: int = Field(ge=SIZE_CHOICES[0], lt=SIZE_CHOICES[-1])


# --------------------------------------------------
def get_args():
    try:
        return GarmentArguments(
            **docopt(
                __doc__.format(
                    color_choices=" ".join(typing.get_args(COLOR_LITERALS)),
                    size_choices=" ".join(str(size) for size in SIZE_CHOICES),
                )
            )
        )
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
