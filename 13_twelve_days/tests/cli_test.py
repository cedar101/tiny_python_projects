#!/usr/bin/env python3
"""tests for twelve_days.py"""

import random
import string
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT
from textwrap import dedent
import tempfile
import itertools

import pytest

prg = "./twelve_days.py"
# prg = "./solution.py"
test_out = Path("./test-out")

day_one = dedent(
    """\
    On the first day of Christmas,
    My true love gave to me,
    A partridge in a pear tree."""
)

day_two = dedent(
    """\
    On the second day of Christmas,
    My true love gave to me,
    Two turtle doves,
    And a partridge in a pear tree."""
)


# --------------------------------------------------
def test_exists():
    """exists"""
    assert Path(prg).is_file()
    assert test_out.exists()


# --------------------------------------------------
@pytest.mark.parametrize("flag", ["-h", "--help"])
def test_usage(flag):
    """usage"""
    out = check_output([prg, flag])
    assert b"usage" in out.lower()


# --------------------------------------------------
@pytest.mark.parametrize("n", [random.randrange(-10, 1), random.randrange(13, 20)])
def test_bad_num(n):
    """test bad number"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-n", str(n)], text=True, stderr=STDOUT)
    assert f'--num "{n}" must be between 1 and 12' in excinfo.value.stdout


# --------------------------------------------------
def test_one():
    """test one"""

    out = check_output([prg, "-n", "1"], text=True)
    assert out.rstrip() == day_one


# --------------------------------------------------
def test_two():
    """test two"""

    out = check_output([prg, "--num", "2"], text=True)
    assert out.rstrip() == f"{day_one}\n\n{day_two}"


# --------------------------------------------------
def test_all_stdout():
    """test"""

    out = check_output([prg], text=True).splitlines()
    assert len(out) == 113
    assert out[0] == "On the first day of Christmas,"
    assert out[-1] == "And a partridge in a pear tree."


# --------------------------------------------------
@pytest.mark.parametrize("n", range(1, 13))
def test_all(n):
    """Test 1-12"""
    # Normal run (STDOUT)
    expected_file = test_out / f"{n}.out"
    assert expected_file.is_file()
    with open(expected_file) as f:
        expected = f.read().rstrip()

    cmd = [prg, "-n", str(n)]
    out = check_output(cmd, text=True).rstrip()
    assert out == expected

    # Run with --outfile
    with tempfile.NamedTemporaryFile("w+") as out_file:
        assert not check_output(
            list(itertools.chain(cmd, ["-o", out_file.name])), text=True
        ).rstrip()
        output = out_file.read().rstrip()
        assert len(output.split("\n")) == len(expected.split("\n"))
        assert output.rstrip() == expected.rstrip()
