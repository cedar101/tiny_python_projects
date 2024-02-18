#!/usr/bin/env python3
"""
usage: nargs+.py [-h] <num>...

positional arguments:
  num         Numbers

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
    numbers = args.num_

    print(f"{' + '.join(numbers)} = {sum(Decimal(num) for num in numbers)}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
