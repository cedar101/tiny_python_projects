#!/usr/bin/env python3
"""tests for gashlycrumb.py"""

import random
import string
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT
import logging

import pytest

logger = logging.getLogger("test")

programs = [f"./{p}" for p in Path(".").glob("solution*.py")]


# --------------------------------------------------
@pytest.fixture()
def file_flag():
    """Either -f or --file"""

    return random.choice(("-f", "--file"))


# --------------------------------------------------
@pytest.fixture(name="bad")
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


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
def test_bad_file(prg, file_flag, bad):
    """bad_file"""
    letter = random.choice(string.ascii_lowercase)
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, letter, file_flag, bad], text=True, stderr=STDOUT)
    logging.info(excinfo.value.output)
    assert f"No such file or directory" in str(excinfo.value.output)


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("a", "A is for Amy who fell down the stairs."),
        ("y", "Y is for Yorick whose head was bashed in."),
    ],
)
def test_one_gashlycrumb(prg, test_input, expected):
    """Test for 'The Gashlycrumb Tinies'"""

    out = check_output([prg, test_input], text=True)
    assert out.strip() == expected


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_two_gashlycrumb(prg):
    """Test for 'The Gashlycrumb Tinies'"""
    expected = "B is for Basil assaulted by bears.\nC is for Clara who wasted away."
    out = check_output([prg, "b", "c"], text=True)
    assert out.strip() == expected


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_three_alternate(prg, file_flag):
    """Test for 'o' from 'alternate.txt'"""

    out = check_output([prg, "o", "P", "q", file_flag, "alternate.txt"], text=True)
    expected = (
        "O is for Orville, who fell in a canyon.\n"
        "P is for Paul, strangled by his banyan.\n"
        "Q is for Quintanna, flayed in the night."
    )
    assert out.strip() == expected


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_bad_letter(prg):
    """Test for bad input"""

    out = check_output([prg, "5", "CH"], text=True)
    expected = 'I do not know "5".\nI do not know "CH".'
    assert out.strip() == expected
