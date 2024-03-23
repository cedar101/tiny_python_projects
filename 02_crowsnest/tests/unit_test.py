#!/usr/bin/env python3
"""tests for crowsnest.py"""

from pathlib import Path

import pytest

from pronunciation_dictionary import (
    DeserializationOptions,
    MultiprocessingOptions,
    load_dict,
)

from crowsnest import choose_article, choose_article_dict


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


vowel_words = ["aviso", "eel", "iceberg", "octopus", "upbound", "hour", "honor", "heir"]


template = "{} {}"


@pytest.fixture(scope="session")
def dictionary():
    return load_dict(
        Path("data/cmudict.dict"),
        "ISO-8859-1",
        DeserializationOptions(False, True, True, False),
        MultiprocessingOptions(8, None, 10000),
    )


# --------------------------------------------------
@pytest.mark.parametrize("word", consonant_words)
def test_consonant(word):
    """brigantine -> a brigantine"""
    assert choose_article(word) == "a"


# --------------------------------------------------
@pytest.mark.parametrize("word", consonant_words)
def test_consonant_upper(word):
    """brigantine -> A Brigantine"""
    assert choose_article(word.title()) == "A"


# --------------------------------------------------
@pytest.mark.parametrize("word", vowel_words)
def test_vowel(word):
    """octopus -> an octopus"""
    assert choose_article(word) == "an"


# --------------------------------------------------
@pytest.mark.parametrize("word", vowel_words)
def test_vowel_upper(word):
    """octopus -> an Octopus"""
    assert choose_article(word.title()) == "An"


# --------------------------------------------------
@pytest.mark.parametrize("word", consonant_words)
def test_consonant_dict(word, dictionary):
    """brigantine -> a brigantine"""
    assert choose_article_dict(word, dictionary) == "a"


# --------------------------------------------------
@pytest.mark.parametrize("word", consonant_words)
def test_consonant_upper_dict(word, dictionary):
    """brigantine -> a Brigantine"""
    assert choose_article_dict(word.title(), dictionary) == "A"


# --------------------------------------------------
@pytest.mark.parametrize("word", vowel_words)
def test_vowel_dict(word, dictionary):
    """octopus -> an octopus"""
    assert choose_article_dict(word, dictionary) == "an"


# --------------------------------------------------
@pytest.mark.parametrize("word", vowel_words)
def test_vowel_upper_dict(word, dictionary):
    """octopus -> an Octopus"""
    assert choose_article_dict(word.title(), dictionary) == "An"
