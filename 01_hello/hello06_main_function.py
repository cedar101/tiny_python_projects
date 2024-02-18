#!/usr/bin/env python3
"""
usage: hello06_main_function.py [-h] [-n NAME]

Say hello

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name to greet [default: World]
"""

# import argparse

from docopt import docopt
from box import Box


def main():
    # parser = argparse.ArgumentParser(description="Say hello")
    # parser.add_argument(
    #     "-n", "--name", metavar="name", default="World", help="Name to greet"
    # )
    # args = parser.parse_args()

    args = Box(docopt(__doc__))

    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
