#!/usr/bin/env python3
"""tests for crowsnest.py"""

import pytest

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


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""
    for word in consonant_words:
        assert choose_article(word) == "a"


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> A Brigantine"""
    for word in consonant_words:
        assert choose_article(word.title()) == "A"


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""
    for word in vowel_words:
        assert choose_article(word) == "an"


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""
    for word in vowel_words:
        assert choose_article(word.title()) == "An"


# --------------------------------------------------
def test_consonant_dict():
    """brigantine -> a brigantine"""
    for word in consonant_words:
        assert choose_article_dict(word) == "a"


# --------------------------------------------------
def test_consonant_upper_dict():
    """brigantine -> a Brigantine"""
    for word in consonant_words:
        assert choose_article_dict(word.title()) == "a"


# --------------------------------------------------
def test_vowel_dict():
    """octopus -> an octopus"""
    for word in vowel_words:
        assert choose_article_dict(word) == "an"


# --------------------------------------------------
def test_vowel_upper_dict():
    """octopus -> an Octopus"""
    for word in vowel_words:
        assert choose_article_dict(word.title()) == "an"
