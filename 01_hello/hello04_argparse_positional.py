#!/usr/bin/env python3
"""
usage: hello04_argparse_positional.py [-h] <name>

Say hello

positional arguments:
  <name>        Name to greet

options:
  -h, --help  show this help message and exit
"""

# import argparse

# parser = argparse.ArgumentParser(description="Say hello")
# parser.add_argument("name", help="Name to greet")
# args = parser.parse_args()

# from argopt import argopt

# parser = argopt(__doc__)  # , version=__version__)
# args = parser.parse_args()

from docopt import docopt
from box import Box

args = Box(docopt(__doc__))  # , version=__version__)

print(f"Hello, {args.name_}!")
