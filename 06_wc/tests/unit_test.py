#!/usr/bin/env python3
"""tests for wc.py"""

from pathlib import Path

import pytest

from wc import wc_1file

empty = "inputs/empty.txt"
one_line = "inputs/one.txt"
two_lines = "inputs/two.txt"
fox = "../inputs/fox.txt"
sonnet = "../inputs/sonnet-29.txt"


# --------------------------------------------------
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (empty, (0, 0, 0)),
        (one_line, (1, 1, 2)),
        (two_lines, (2, 2, 4)),
        (fox, (1, 9, 45)),
        (sonnet, (17, 118, 661)),
    ],
)
def test_wc_1file(test_input, expected):
    with Path(test_input).open() as f:
        assert wc_1file(f) == expected
