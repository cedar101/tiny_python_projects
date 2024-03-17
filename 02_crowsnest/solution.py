#!/usr/bin/env python3
"""
usage: solution.py [-h] [(--larboard|--starboard)] <word>...

Crow's Nest -- choose the correct article

positional arguments:
  	<word>        A word

options:
  	-h, --help            show this help message and exit
  	--larboard            좌현(左舷)
  	--starboard           우현(右舷)
"""

from pathlib import *

from box import Box
from docopt import docopt, DocoptExit
from pronunciation_dictionary import (
    DeserializationOptions,
    MultiprocessingOptions,
    load_dict,
)

from crowsnest import choose_article, choose_article_dict


# --------------------------------------------------
def get_args():
    return Box(docopt(__doc__))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    side = "starboard" if args.starboard else "larboard"
    words = args.word_

    dictionary = load_dict(
        Path("data/cmudict.dict"),
        "ISO-8859-1",
        DeserializationOptions(False, True, True, False),
        MultiprocessingOptions(8, None, 10000),
    )

    for word in words:
        article = choose_article_dict(word, dictionary)
        print(f"Ahoy, Captain, {article} {word} off the {side} bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
