#!/usr/bin/env python3
"""tests for picnic.py"""

from pathlib import Path
from subprocess import check_output

import pytest


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
            out = check_output([prg, flag])
            assert b"usage" in out.lower()


# --------------------------------------------------
def test_one(programs):
    """one item"""
    for prg in programs:
        out = check_output([prg, "chips"])
        assert out.strip() == b"You are bringing chips."


# --------------------------------------------------
def test_two(programs):
    """two items"""
    for prg in programs:
        out = check_output([prg, "soda", "french fries"])
        assert out.strip() == b"You are bringing soda and french fries."


# --------------------------------------------------
def test_more_than_two_serial(programs):
    """more than two items"""
    for prg in programs:
        args = ["potato chips", "coleslaw", "cupcakes", "French silk pie"]
        out = check_output([prg, "--serial"] + args)
        expected = (
            b"You are bringing potato chips, coleslaw, cupcakes, and French silk pie."
        )
        assert out.strip() == expected


# --------------------------------------------------
def test_more_than_two_no_serial(programs):
    """more than two items"""
    for prg in programs:
        args = ["potato chips", "coleslaw", "cupcakes", "French silk pie"]
        out = check_output([prg] + args)
        expected = (
            b"You are bringing potato chips, coleslaw, cupcakes and French silk pie."
        )
        assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted(programs):
    """two items sorted output"""
    for prg in programs:
        out = check_output([prg, "--sort", "soda", "candy"])
        assert out.strip() == b"You are bringing candy and soda."


# --------------------------------------------------
def test_more_than_two_sorted_serial(programs):
    """more than two items sorted output"""
    for prg in programs:
        args = ["bananas", "apples", "dates", "cherries"]
        out = check_output([prg, "--sort", "--serial"] + args)
        expected = b"You are bringing apples, bananas, cherries, and dates."
        assert out.strip() == expected


# --------------------------------------------------
def test_more_than_two_sorted_no_serial(programs):
    """more than two items sorted output"""
    for prg in programs:
        args = ["bananas", "apples", "dates", "cherries"]
        out = check_output([prg, "--sort"] + args, text=True)
        expected = "You are bringing apples, bananas, cherries and dates."
        assert out.strip() == expected
