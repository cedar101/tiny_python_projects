#!/usr/bin/env python3
"""tests for wc.py"""

import random
import string
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT
import logging

import pytest


logger = logging.getLogger("test")

empty = "inputs/empty.txt"
one_line = "inputs/one.txt"
two_lines = "inputs/two.txt"
fox = "../inputs/fox.txt"
sonnet = "../inputs/sonnet-29.txt"

programs = [f"./{p}" for p in Path(".").glob("solution*.py")]


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
def test_bad_file(prg, bad):
    """bad_file"""

    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, bad], text=True, stderr=STDOUT)
    logging.info(excinfo.value.output)
    assert f"No such file or directory: '{bad}'" in str(excinfo.value.output)


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_empty(prg):
    """Test on empty"""

    out = check_output([prg, empty], text=True)
    assert f"       0       0       0 {empty}" in out


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_one(prg):
    """Test on one"""

    out = check_output([prg, one_line], text=True)
    assert f"       1       1       2 {one_line}" in out


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_two(prg):
    """Test on two"""

    out = check_output([prg, two_lines], text=True)
    assert f"       2       2       4 {two_lines}" in out


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_fox(prg):
    """Test on fox"""

    out = check_output([prg, fox], text=True)
    assert f"       1       9      45 {fox}" in out


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_more(prg):
    """Test on more than one file"""

    out = check_output([prg, fox, sonnet], text=True)
    expected = (
        f"       1       9      45 {fox}\n"
        f"      17     118     661 {sonnet}\n"
        "      18     127     706 total"
    )
    assert expected in out


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_stdin(prg):
    """Test on stdin"""

    out = check_output(f"{prg} < {fox}", shell=True, text=True)
    assert "       1       9      45 <stdin>" in out
