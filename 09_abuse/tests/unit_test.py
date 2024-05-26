#!/usr/bin/env python3
"""tests for abuse.py"""

from textwrap import dedent

from abuse import insult


# --------------------------------------------------
def test_01():
    """test"""

    out = "\n".join(insult(seed=1, number=1))
    assert out == "You filthsome, cullionly fiend!"


# --------------------------------------------------
def test_02():
    """test"""

    out = "\n".join(insult(seed=2))
    expected = dedent(
        """
        You corrupt, detestable beggar!
        You peevish, foolish gull!
        You insatiate, heedless worm!
        """
    ).strip()
    assert out == expected


# --------------------------------------------------
def test_03():
    """test"""

    out = "\n".join(insult(seed=3, number=5, adjectives=1))
    expected = dedent(
        """
        You infected villain!
        You vile braggart!
        You peevish worm!
        You sodden-witted villain!
        You cullionly worm!
        """
    ).strip()
    assert out == expected


# --------------------------------------------------
def test_04():
    """test"""

    out = "\n".join(insult(seed=4, number=2, adjectives=4))
    expected = dedent(
        """
        You infected, lecherous, dishonest, rotten recreant!
        You filthy, detestable, cullionly, base lunatic!
        """
    ).strip()
    assert out == expected
