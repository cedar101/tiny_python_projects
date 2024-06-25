#!/usr/bin/env python3
"""tests for bottles.py"""

import hashlib
import random
import string
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT
from textwrap import dedent

import pytest

prg = "./bottles.py"

with open("sums.txt") as f:
    sums = dict(x.rstrip().split("\t") for x in f)  # .read().splitlines())


# --------------------------------------------------
@pytest.fixture(name="bad_str")
def random_string() -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
@pytest.fixture(name="bad_int")
def random_negative_integer() -> int:
    return random.randint(-10, 0)


# --------------------------------------------------
@pytest.fixture(name="bad_float")
def random_float() -> float:
    return round(random.uniform(0, 10), random.randint(1, 10))


# --------------------------------------------------
def test_exists():
    """exists"""
    assert Path(prg).is_file()


# --------------------------------------------------
@pytest.mark.parametrize("flag", ["-h", "--help"])
def test_usage(flag):
    """usage"""
    out = check_output([prg, flag])
    assert b"usage" in out.lower()


# --------------------------------------------------
def test_string(bad_str):
    """str value"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-n", bad_str], text=True, stderr=STDOUT)
    assert "usage" in excinfo.value.stdout.lower()
    assert f"invalid int value: '{bad_str}'" in excinfo.value.stdout


# --------------------------------------------------
def test_bad_int(bad_int):
    """Bad integer value"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-n", str(bad_int)], text=True, stderr=STDOUT)
    assert "usage" in excinfo.value.stdout.lower()
    assert f'--num "{bad_int}" must be greater than 0' in excinfo.value.stdout


# --------------------------------------------------
def test_float(bad_float):
    """float value"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "--num", str(bad_float)], text=True, stderr=STDOUT)
    assert "usage" in excinfo.value.stdout.lower()
    assert f"invalid int value: '{bad_float}'" in excinfo.value.stdout


# --------------------------------------------------
def test_one():
    """One bottle of beer"""

    expected = dedent(
        """\
        1 bottle of beer on the wall,
        1 bottle of beer,
        Take one down, pass it around,
        No more bottles of beer on the wall!
        """
    )

    out = check_output([prg, "--num", "1"], text=True)
    assert out == expected


# --------------------------------------------------
def test_two():
    """Two bottles of beer"""

    expected = dedent(
        """\
        2 bottles of beer on the wall,
        2 bottles of beer,
        Take one down, pass it around,
        1 bottle of beer on the wall!
        
        1 bottle of beer on the wall,
        1 bottle of beer,
        Take one down, pass it around,
        No more bottles of beer on the wall!
        """
    )

    out = check_output([prg, "-n", "2"], text=True)
    assert out == expected


# --------------------------------------------------
def test_two_reversed():
    """Two bottles of beer"""

    expected = dedent(
        """\
        1 bottle of beer on the wall,
        1 bottle of beer,
        Take one down, pass it around,
        No more bottles of beer on the wall!
        
        2 bottles of beer on the wall,
        2 bottles of beer,
        Take one down, pass it around,
        1 bottle of beer on the wall!
        """
    )

    out = check_output([prg, "-r", "-n", "2"], text=True)
    assert out == expected


# --------------------------------------------------
@pytest.mark.parametrize("n", random.choices(list(sums.keys()), k=10))
def test_random(n):
    """Random number"""
    flag = random.choice(["-n", "--num"])
    out = check_output([prg, flag, n], text=True)
    # out += "\n"  # because the last newline is removed
    # breakpoint()
    assert hashlib.md5(out.encode("utf-8")).hexdigest() == sums[n]
