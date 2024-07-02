#!/usr/bin/env python3
"""
usage: twelve_days.py [-h] [-e] [-n DAYS] [-o FILE]

Twelve Days of Christmas

options:
  -h, --help                show this help message and exit
  -n DAYS, --num=DAYS       Number of days to sing [type: int] [default: 12] [choices: {day_choices}]
  -o FILE, --outfile=FILE   Output file [type: path]
  -e, --emoji               print lyrics using emoji
"""
import sys
from pathlib import Path

from type_docopt import docopt, DocoptExit
from box import Box
import emoji


ORDINAL = [
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

GIFTS = [
    [
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
    ],
    [
        "A :bird: in a pear tree.",
        "Two turtle :swan:s,",
        "Three French :chicken:s,",
        "Four calling :bird:s,",
        "Five gold :ring:s,",
        "Six :bird:s a laying,",
        "Seven :bird:s a swimming,",
        "Eight :woman:s a milking,",
        "Nine :woman:s dancing,",
        "Ten :man:s a leaping,",
        "Eleven :man:s piping,",
        "Twelve :drum:s drumming,",
    ],
]


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
    verses = (verse(n, args.emoji) for n in range(1, args.num + 1))

    lyric = "\n\n".join(verses)
    with args.outfile.open("w") if args.outfile else sys.stdout as outfile:
        print(lyric, file=outfile)


# --------------------------------------------------
def verse(day, use_emoji=False):
    """Create a verse"""
    lines = [f"On the {ORDINAL[day - 1]} day of Christmas,", "My true love gave to me,"]
    lines.extend(GIFTS[int(use_emoji)][day - 1 :: -1])
    # reversed(GIFTS[int(use_emoji)][:day]))

    if day > 1:
        lines[-1] = f"And {lines[-1].lower()}"

    result = "\n".join(lines)
    return emoji.emojize(result) if use_emoji else result


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
