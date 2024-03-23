#!/usr/bin/env python3
"""
usage: solution.py [-h] [-s] <item>...

Picnic game

positional arguments:
  <item>           Item(s) to bring

options:
  -h, --help    show this help message and exit
  -s, --sorted  Sort the items [default: False]
"""

from box import Box
from docopt import docopt

from picnic import serial_comma


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    return Box(docopt(__doc__))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item_

    if args.sorted:
        items.sort()

    bringing = serial_comma(items)
    print("You are bringing {}.".format(bringing))


# --------------------------------------------------
if __name__ == "__main__":
    main()
