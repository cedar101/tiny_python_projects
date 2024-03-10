#!/usr/bin/env python3
"""
usage: nargs2.py [-h] <num> <num>

positional arguments:
  <num>         Numbers

options:
  -h, --help  show this help message and exit
"""
from decimal import Decimal

from docopt import docopt
from box import Box


# --------------------------------------------------
def get_args():
    return Box(docopt(__doc__))


# --------------------------------------------------
def main():
    args = get_args()
    n1, n2 = args.num_
    # print(f"{n1} + {n2} = {float(n1) + float(n2)}")
    print(f"{n1} + {n2} = {Decimal(n1) + Decimal(n2)}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
