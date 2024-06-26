#!/usr/bin/env python3
"""tests for picnic.py"""

import pytest

from picnic import english_enumerate


# --------------------------------------------------
def test_one():
    """one item"""
    assert english_enumerate(["chips"]) == "chips"


# --------------------------------------------------
def test_two():
    """two items"""
    assert english_enumerate(["soda", "french fries"]) == "soda and french fries"


# --------------------------------------------------
def test_more_than_two_no_serial():
    """more than two items"""
    assert (
        english_enumerate(["potato chips", "coleslaw", "cupcakes", "French silk pie"])
        == "potato chips, coleslaw, cupcakes and French silk pie"
    )


# --------------------------------------------------
def test_more_than_two_serial():
    """more than two items"""
    assert (
        english_enumerate(
            ["potato chips", "coleslaw", "cupcakes", "French silk pie"],
            serial_comma=True,
        )
        == "potato chips, coleslaw, cupcakes, and French silk pie"
    )
