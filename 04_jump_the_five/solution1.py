#!/usr/bin/env python3
"""Jump the Five"""

import argparse
import io


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def jump_the_five(text: str) -> str:
    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }
    with io.StringIO() as output:
        for char in text:
            print(jumper.get(char, char), end="", file=output)
        return output.getvalue()


def main():
    """Make a jazz noise here"""

    args = get_args()
    print(jump_the_five(args.text))


# --------------------------------------------------
if __name__ == "__main__":
    main()
