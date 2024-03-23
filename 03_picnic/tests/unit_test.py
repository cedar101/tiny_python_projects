#!/usr/bin/env python3
"""tests for picnic.py"""

import pytest

from picnic import serial_comma, no_serial_comma


# --------------------------------------------------
def test_one():
    """one item"""
    assert serial_comma(["chips"]) == "chips"


# --------------------------------------------------
def test_two():
    """two items"""
    assert serial_comma(["soda", "french fries"]) == "soda and french fries"


# --------------------------------------------------
def test_more_than_two_no_serial():
    """more than two items"""
    assert (
        no_serial_comma(["potato chips", "coleslaw", "cupcakes", "French silk pie"])
        == "potato chips, coleslaw, cupcakes and French silk pie"
    )


# --------------------------------------------------
def test_more_than_two_serial():
    """more than two items"""
    assert (
        serial_comma(["potato chips", "coleslaw", "cupcakes", "French silk pie"])
        == "potato chips, coleslaw, cupcakes, and French silk pie"
    )
