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

from picnic import serial_comma, no_serial_comma


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

    if args.serial or args.oxford:
        bringing = serial_comma(items)
    else:
        bringing = no_serial_comma(items)
    print("You are bringing {}.".format(bringing))


# --------------------------------------------------
if __name__ == "__main__":
    main()
