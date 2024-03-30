#!/usr/bin/env python3
"""
usage: solution.py [-h] [--sort | --sorted] [--serial | --oxford] <item>...

Picnic game

positional arguments:
  <item>              Item(s) to bring

options:
  -h, --help          Show this help message and exit
  --sort, --sorted    Sort the items [default: False]
  --serial, --oxford  Use serial comma (Oxford comma)
"""

from box import Box
from docopt import docopt

from picnic import english_enumerate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    return Box(docopt(__doc__))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item_

    if args.sort or args.sorted:
        items.sort()

    bringing = english_enumerate(items, args.serial or args.oxford)
    print("You are bringing {}.".format(bringing))


# --------------------------------------------------
if __name__ == "__main__":
    main()
