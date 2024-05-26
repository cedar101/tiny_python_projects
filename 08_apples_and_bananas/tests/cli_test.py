#!/usr/bin/env python3
"""tests for apples.py"""

from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT
import logging

import pytest

logger = logging.getLogger("test")

programs = [f"./{p}" for p in Path(".").glob("solution*.py")]

# prg = "./apples.py"
fox = "../inputs/fox.txt"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_exists(prg):
    """exists"""
    assert Path(prg).is_file()


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_usage(prg):
    """usage"""

    for flag in ["-h", "--help"]:
        out = check_output([prg, flag])
        assert b"usage" in out.lower()


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_bad_vowel(prg):
    """Should fail on a bad vowel"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-v", "x", "foo"], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_command_line(prg):
    """foo -> faa"""

    out = check_output([prg, "foo"])
    assert out.strip() == b"faa"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_command_line_with_vowel(prg):
    """foo -> fii"""

    out = check_output([prg, "-v", "i", "foo"])
    assert out.strip() == b"fii"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_command_line_with_vowel_preserve_case(prg):
    """foo -> fii"""

    out = check_output([prg, "APPLES AND BANANAS", "--vowel", "i"])
    assert out.strip() == b"IPPLIS IND BININIS"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_file(prg):
    """fox.txt"""

    out = check_output([prg, fox])
    assert out.strip() == b"Tha qaack brawn fax jamps avar tha lazy dag."


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_file_with_vowel(prg):
    """fox.txt"""

    out = check_output([prg, "--vowel", "o", fox])
    assert out.strip() == b"Tho qoock brown fox jomps ovor tho lozy dog."
