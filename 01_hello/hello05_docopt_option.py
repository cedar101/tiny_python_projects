#!/usr/bin/env python3
"""
usage: hello05_argparse_option.py [-h] [-n NAME]

Say hello

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name to greet [default: World]
"""

# import argparse

# parser = argparse.ArgumentParser(description='Say hello')
# parser.add_argument('-n', '--name', metavar='name',
#                     default='World', help='Name to greet')
# args = parser.parse_args()

from docopt import docopt
from box import Box

args = Box(docopt(__doc__))

print(f"Hello, {args.name}!")
