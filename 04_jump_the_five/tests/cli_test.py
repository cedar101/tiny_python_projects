#!/usr/bin/env python3
"""tests for jump.py"""

from pathlib import Path
from subprocess import check_output

import pytest


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
@pytest.mark.parametrize("prg", programs)
def test_01(prg):
    """test"""
    out = check_output([prg, "123-456-7890"])
    assert out.rstrip() == b"987-604-3215"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_02(prg):
    """test"""
    out = check_output([prg, "That number to call is 098-765-4321."])
    assert out.rstrip() == b"That number to call is 512-340-6789."
