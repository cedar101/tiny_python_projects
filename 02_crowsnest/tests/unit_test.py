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


template = "{} {}"


@pytest.fixture
def dictionary():
    return load_dict(
        Path("data/cmudict.dict"),
        "ISO-8859-1",
        DeserializationOptions(False, True, True, False),
        MultiprocessingOptions(8, None, 10000),
    )


# --------------------------------------------------
def test_consonant(consonant_words):
    """brigantine -> a brigantine"""
    for word in consonant_words:
        assert choose_article(word) == "a"


# --------------------------------------------------
def test_consonant_upper(consonant_words):
    """brigantine -> A Brigantine"""
    for word in consonant_words:
        assert choose_article(word.title()) == "A"


# --------------------------------------------------
def test_vowel(vowel_words):
    """octopus -> an octopus"""
    for word in vowel_words:
        assert choose_article(word) == "an"


# --------------------------------------------------
def test_vowel_upper(vowel_words):
    """octopus -> an Octopus"""
    for word in vowel_words:
        assert choose_article(word.title()) == "An"


# --------------------------------------------------
def test_consonant_dict(consonant_words, dictionary):
    """brigantine -> a brigantine"""
    for word in consonant_words:
        assert choose_article_dict(word, dictionary) == "a"


# --------------------------------------------------
def test_consonant_upper_dict(consonant_words, dictionary):
    """brigantine -> a Brigantine"""
    for word in consonant_words:
        assert choose_article_dict(word.title(), dictionary) == "A"


# --------------------------------------------------
def test_vowel_dict(vowel_words, dictionary):
    """octopus -> an octopus"""
    for word in vowel_words:
        assert choose_article_dict(word, dictionary) == "an"


# --------------------------------------------------
def test_vowel_upper_dict(vowel_words, dictionary):
    """octopus -> an Octopus"""
    for word in vowel_words:
        assert choose_article_dict(word.title(), dictionary) == "An"
