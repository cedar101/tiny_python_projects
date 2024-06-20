#!/usr/bin/env python3
"""tests for ransom.py"""

import random
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT


import pytest


programs = [f"./{p}" for p in Path(".").glob("solution*.py")]
fox = "../inputs/fox.txt"
now = "../inputs/now.txt"


# --------------------------------------------------
@pytest.fixture
def seed_flag():
    return random.choice(("-s", "--seed"))


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_exists(prg):
    """exists"""
    assert Path(prg).is_file()


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
@pytest.mark.parametrize("flag", ["-h", "--help"])
def test_usage(prg, flag):
    """usage"""
    out = check_output([prg, flag])
    assert b"usage" in out.lower()


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
@pytest.mark.parametrize(
    "seed,expected",
    [
        ("1", "thE QUICk BrOWn Fox jumpS OveR tHe LAzY dOg."),
        ("3", "thE quICk BROwn Fox jUmPS OVEr the lAZY DOG."),
    ],
)
def test_text1(prg, seed_flag, seed, expected):
    in_text = "The quick brown fox jumps over the lazy dog."
    out = check_output([prg, seed_flag, seed, in_text], text=True)
    assert out.strip() == expected


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
@pytest.mark.parametrize(
    "seed,expected",
    [
        ("2", "now iS the TIME fOR ALl good meN TO COMe To THE AID oF THE PArTY."),
        ("5", "NOw is tHE Time FOr all good men To coME TO tHe AiD OF THe ParTy."),
    ],
)
def test_text2(prg, seed_flag, seed, expected):
    in_text = "Now is the time for all good men to come to the aid of the party."
    out = check_output([prg, seed_flag, seed, in_text], text=True)
    assert out.strip() == expected


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
@pytest.mark.parametrize(
    "filename,seed,expected",
    [
        (fox, "1", "thE QUICk BrOWn Fox jumpS OveR tHe LAzY dOg."),
        (fox, "3", "thE quICk BROwn Fox jUmPS OVEr the lAZY DOG."),
        (now, "2", "now iS the TIME fOR ALl good meN TO COMe To THE AID oF THE PArTY."),
        (now, "5", "NOw is tHE Time FOr all good men To coME TO tHe AiD OF THe ParTy."),
    ],
)
def test_file(prg, seed_flag, filename, seed, expected):
    out = check_output([prg, seed_flag, seed, filename], text=True)
    assert out.strip() == expected
