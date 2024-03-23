#!/usr/bin/env python3
"""tests for picnic.py"""

from pathlib import Path
from subprocess import check_output

import pytest

prg = "./picnic.py"


@pytest.fixture
def programs():
    return [f"./{p}" for p in Path(".").glob("solution*.py")]


# --------------------------------------------------
def test_exists(programs):
    """exists"""
    for prg in programs:
        assert Path(prg).is_file()


# --------------------------------------------------
def test_usage(programs):
    """usage"""
    for prg in programs:
        for flag in ["-h", "--help"]:
            out = check_output([prg, flag], text=True)
            assert "usage" in out.lower()


# --------------------------------------------------
def test_one(programs):
    """one item"""
    for prg in programs:
        out = check_output([prg, "chips"], text=True)
        assert out.strip() == "You are bringing chips."


# --------------------------------------------------
def test_two(programs):
    """two items"""
    for prg in programs:
        out = check_output([prg, "soda", "french fries"], text=True)
        assert out.strip() == "You are bringing soda and french fries."


# --------------------------------------------------
def test_more_than_two(programs):
    """more than two items"""
    for prg in programs:
        args = ["potato chips", "coleslaw", "cupcakes", "French silk pie"]
        out = check_output([prg] + args, text=True)
        expected = (
            "You are bringing potato chips, coleslaw, cupcakes, and French silk pie."
        )
        assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted(programs):
    """two items sorted output"""
    for prg in programs:
        out = check_output([prg, "-s", "soda", "candy"], text=True)
        assert out.strip() == "You are bringing candy and soda."


# --------------------------------------------------
def test_more_than_two_sorted(programs):
    """more than two items sorted output"""
    for prg in programs:
        args = ["bananas", "apples", "dates", "cherries"]
        out = check_output([prg] + args + ["--sorted"], text=True)
        expected = "You are bringing apples, bananas, cherries, and dates."
        assert out.strip() == expected
