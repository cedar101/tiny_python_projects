#!/usr/bin/env python3
"""tests for wc.py"""

import random
import string
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT

import pytest


empty = "./inputs/empty.txt"
one_line = "./inputs/one.txt"
two_lines = "./inputs/two.txt"
fox = "../inputs/fox.txt"
sonnet = "../inputs/sonnet-29.txt"


programs = [f"./{p}" for p in Path(".").glob("solution*.py")]


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
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_bad_file(prg):
    """bad_file"""

    bad = random_string()
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, bad], text=True, stderr=STDOUT)
    assert f"No such file or directory: '{bad}'" in str(excinfo.value.output)


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_empty(prg):
    """Test on empty"""

    out = check_output([prg, empty], text=True)
    assert out.rstrip() == f"       0       0       0 {empty}"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_one(prg):
    """Test on one"""

    out = check_output([prg, one_line])
    assert out.rstrip() == "       1       1       2 {one_line}"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_two(prg):
    """Test on two"""

    out = check_output([prg, two_lines])
    assert out.rstrip() == "       2       2       4 {two_lines}"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_fox(prg):
    """Test on fox"""

    out = check_output([prg, fox])
    assert out.rstrip() == "       1       9      45 {fox}"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_more(prg):
    """Test on more than one file"""

    out = check_output([prg, fox, sonnet])
    expected = (
        f"       1       9      45 {fox}\n"
        f"      17     118     661 {sonnet}\n"
        "      18     127     706 total"
    )
    assert out == expected


# --------------------------------------------------
def test_stdin():
    """Test on stdin"""

    rv, out = getstatusoutput(f"{prg} < {fox}")
    assert rv == 0
    assert out.rstrip() == "       1       9      45 <stdin>"
