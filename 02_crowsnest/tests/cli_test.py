#!/usr/bin/env python3
"""tests for crowsnest.py"""

# import os
from pathlib import Path
from subprocess import check_output

import pytest

prg = "./crowsnest.py"


@pytest.fixture
def consonant_words():
    return [
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


@pytest.fixture
def vowel_words():
    return ["aviso", "eel", "iceberg", "octopus", "upbound", "hour", "honor", "heir"]


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


# --------------------------------------------------
def test_consonant(programs, consonant_words):
    """brigantine -> a brigantine"""
    for prg in programs:
        outputs = check_output([prg] + consonant_words, text=True)
        for out, word in zip(outputs.splitlines(), consonant_words):
            assert out.strip() == template.format("a", word)


# --------------------------------------------------
def test_consonant_upper(programs, consonant_words):
    """brigantine -> a Brigantine"""
    for prg in programs:
        outputs = check_output(
            [prg] + [word.title() for word in consonant_words], text=True
        )
        for out, word in zip(outputs.splitlines(), consonant_words):
            assert out.strip() == template.format("A", word.title())


# --------------------------------------------------
def test_vowel(programs, vowel_words):
    """octopus -> an octopus"""
    for prg in programs:
        outputs = check_output([prg] + vowel_words, text=True)
        for out, word in zip(outputs.splitlines(), vowel_words):
            assert out.strip() == template.format("an", word)


# --------------------------------------------------
def test_vowel_upper(programs, vowel_words):
    """octopus -> an Octopus"""
    for prg in programs:
        outputs = check_output(
            [prg] + [word.title() for word in vowel_words], text=True
        )
        for out, word in zip(outputs.splitlines(), vowel_words):
            assert out.strip() == template.format("An", word.title())
