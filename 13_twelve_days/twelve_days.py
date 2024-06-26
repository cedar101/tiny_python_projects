#!/usr/bin/env python3
"""
usage: twelve_days.py [-h] [-n DAYS] [-o FILE]

Twelve Days of Christmas

options:
  -h, --help                show this help message and exit
  -n DAYS, --num=DAYS       Number of days to sing [type: int] [default: 12] [choices: {day_choices}]
  -o FILE, --outfile=FILE   Output file [type: path]
"""
import sys
from pathlib import Path

from type_docopt import docopt, DocoptExit
from box import Box


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    try:
        args = Box(
            docopt(
                __doc__.format(day_choices=" ".join(str(n) for n in range(1, 13))),
                types={"path": Path},
            )
        )
    except ValueError as exc_not_in:
        # breakpoint()
        num_str, _1, _2 = str(exc_not_in).partition(" ")
        try:
            num = int(num_str)
        except ValueError as exc_invalid:
            _0, _1, invalid = str(exc_invalid).rpartition(" ")
            raise DocoptExit(
                f"error: argument -n/--num: invalid int value: {invalid}"
            ) from exc_invalid
        raise DocoptExit(
            f'error: --num "{num_str}" must be between 1 and 12'
        ) from exc_not_in

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    verses = (verse(n) for n in range(1, args.num + 1))

    with args.outfile.open("w") if args.outfile else sys.stdout as outfile:
        print("\n\n".join(verses), file=outfile)


# --------------------------------------------------
def verse(day):
    """Create a verse"""

    ordinal = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]

    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five gold rings,",
        "Six geese a laying,",
        "Seven swans a swimming,",
        "Eight maids a milking,",
        "Nine ladies dancing,",
        "Ten lords a leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,",
    ]

    lines = [f"On the {ordinal[day - 1]} day of Christmas,", "My true love gave to me,"]

    lines.extend(reversed(gifts[:day]))

    if day > 1:
        lines[-1] = f"And {lines[-1].lower()}"

    return "\n".join(lines)


# --------------------------------------------------
def test_verse():
    """Test verse"""

    assert verse(1) == "\n".join(
        [
            "On the first day of Christmas,",
            "My true love gave to me,",
            "A partridge in a pear tree.",
        ]
    )

    assert verse(2) == "\n".join(
        [
            "On the second day of Christmas,",
            "My true love gave to me,",
            "Two turtle doves,",
            "And a partridge in a pear tree.",
        ]
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
