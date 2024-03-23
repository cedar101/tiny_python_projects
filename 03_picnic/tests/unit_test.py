#!/usr/bin/env python3
"""tests for picnic.py"""

import pytest

from picnic import serial_comma


# --------------------------------------------------
def test_one():
    """one item"""
    assert serial_comma(["chips"]) == "chips"


# --------------------------------------------------
def test_two():
    """two items"""
    assert serial_comma(["soda", "french fries"]) == "soda and french fries"


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""
    assert (
        serial_comma(["potato chips", "coleslaw", "cupcakes", "French silk pie"])
        == "potato chips, coleslaw, cupcakes, and French silk pie"
    )
