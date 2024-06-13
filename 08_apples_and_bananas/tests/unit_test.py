#!/usr/bin/env python3
"""tests for picnic.py"""

import pytest
from pathlib import Path
import importlib


modules = [importlib.import_module(p.stem) for p in Path(".").glob("solution*.py")]


# --------------------------------------------------
@pytest.mark.parametrize("solution", modules)
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("foo", "faa"),
        (
            "The quick brown fox jumps over the lazy dog.",
            "Tha qaack brawn fax jamps avar tha lazy dag.",
        ),
    ],
)
def test_default_vowel(solution, test_input, expected):
    assert solution.replace_vowels(test_input) == expected


# --------------------------------------------------
@pytest.mark.parametrize("solution", modules)
@pytest.mark.parametrize(
    "test_input,vowel,expected",
    [
        ("foo", "i", "fii"),
        ("APPLES AND BANANAS", "i", "IPPLIS IND BININIS"),
        (
            "The quick brown fox jumps over the lazy dog.",
            "o",
            "Tho qoock brown fox jomps ovor tho lozy dog.",
        ),
    ],
)
def test_with_setting_vowel(solution, test_input, vowel, expected):
    assert solution.replace_vowels(test_input, vowel) == expected
