#!/usr/bin/env python3
"""
usage: twelve_days.py [-h] [-n DAYS] [-o FILE]

Twelve Days of Christmas

options:
  -h, --help                show this help message and exit
  -n DAYS, --num DAYS       Number of days to sing [type: int] [default: 12] [choices: {day_choices}]
  -o FILE, --outfile FILE   Output file [type: path]
"""
from pathlib import Path

from type_docopt import docopt, DocoptExit
from box import Box


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    try:
        args = Box(
            docopt(__doc__.format(day_choices=" ".join(str(n) for n in range(1, 13))))
        )
    except ValueError as e:
        strerr = str(e)
        if "invalid literal for int() with base 10" in strerr:
            _0, _1, invalid_literal = strerr.rpartition(" ")
            strerr = f"invalid int value: {invalid_literal}"
        raise DocoptExit(f"error: {strerr}") from e
    # if args.num not in range(1, 13):
    #     parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    verses = map(verse, range(1, args.num + 1))
    print("\n\n".join(verses), file=args.outfile)


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
        lines[-1] = "And " + lines[-1].lower()

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
