#!/usr/bin/env python3
"""tests for crowsnest.py"""

# import os
from pathlib import Path
from subprocess import check_output

import pytest

prg = "./crowsnest.py"
consonant_words = [
    "brigantine",
    "clipper",
    "dreadnought",
    "frigate",
    "galleon",
    "haddock",
    "junk",
    "ketch",
    "longboat",
    "mullet",
    "narwhal",
    "porpoise",
    "quay",
    "regatta",
    "submarine",
    "tanker",
    "vessel",
    "whale",
    "xebec",
    "yatch",
    "zebrafish",
]
vowel_words = ["aviso", "eel", "iceberg", "octopus", "upbound", "heir", "honor", "hour"]
template = "Ahoy, Captain, {} {} off the larboard bow!"


@pytest.fixture
def programs():
    return [f"./{p}" for p in Path(".").glob("solution*.py")]


# --------------------------------------------------
def test_exists(programs):
    """exists"""
    # assert os.path.isfile(prg)
    for prg in programs:
        assert Path(prg).is_file()


# --------------------------------------------------
def test_usage(programs):
    """usage"""
    for prg in programs:
        for flag in ["-h", "--help"]:
            out = check_output([prg, flag], text=True)
            assert "usage" in out.lower()
            # assert out.lower().startswith("usage")


# --------------------------------------------------
def test_consonant(programs):
    """brigantine -> a brigantine"""
    for prg in programs:
        for word in consonant_words:
            out = check_output([prg, word], text=True)
            assert out.strip() == template.format("a", word)


# --------------------------------------------------
def test_consonant_upper(programs):
    """brigantine -> a Brigantine"""
    for prg in programs:
        for word in consonant_words:
            out = check_output([prg, word.title()], text=True)
            assert out.strip() == template.format("A", word.title())


# --------------------------------------------------
def test_vowel(programs):
    """octopus -> an octopus"""
    for prg in programs:
        for word in vowel_words:
            out = check_output([prg, word], text=True)
            assert out.strip() == template.format("an", word)


# --------------------------------------------------
def test_vowel_upper(programs):
    """octopus -> an Octopus"""
    for prg in programs:
        for word in vowel_words:
            out = check_output([prg, word.upper()], text=True)
            assert out.strip() == template.format("An", word.upper())
