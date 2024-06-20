#!/usr/bin/env python3
"""tests for ransom.py"""

import random
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT


import pytest


programs = [f"./{p}" for p in Path(".").glob("solution*.py")]

fox_text = "The quick brown fox jumps over the lazy dog."
now_text = "Now is the time for all good men to come to the aid of the party."
fox_file = "../inputs/fox.txt"
now_file = "../inputs/now.txt"


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
    "in_text,seed,expected",
    [
        (fox_text, "1", "thE QUICk BrOWn Fox jumpS OveR tHe LAzY dOg."),
        (fox_text, "3", "thE quICk BROwn Fox jUmPS OVEr the lAZY DOG."),
        (
            now_text,
            "2",
            "now iS the TIME fOR ALl good meN TO COMe To THE AID oF THE PArTY.",
        ),
        (
            now_text,
            "5",
            "NOw is tHE Time FOr all good men To coME TO tHe AiD OF THe ParTy.",
        ),
    ],
)
def test_text(prg, seed_flag, in_text, seed, expected):
    out = check_output([prg, seed_flag, seed, in_text], text=True)
    assert out.strip() == expected


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
@pytest.mark.parametrize(
    "filename,seed,expected",
    [
        (fox_file, "1", "thE QUICk BrOWn Fox jumpS OveR tHe LAzY dOg."),
        (fox_file, "3", "thE quICk BROwn Fox jUmPS OVEr the lAZY DOG."),
        (
            now_file,
            "2",
            "now iS the TIME fOR ALl good meN TO COMe To THE AID oF THE PArTY.",
        ),
        (
            now_file,
            "5",
            "NOw is tHE Time FOr all good men To coME TO tHe AiD OF THe ParTy.",
        ),
    ],
)
def test_file(prg, seed_flag, filename, seed, expected):
    out = check_output([prg, seed_flag, seed, filename], text=True)
    assert out.strip() == expected
