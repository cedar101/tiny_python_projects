#!/usr/bin/env python3
"""tests for picnic.py"""

import pytest

import solution1, solution2, solution3, solution4, solution5


# --------------------------------------------------
@pytest.mark.parametrize(
    "solution", [solution1, solution2, solution3, solution4, solution5]
)
def test_01(solution):
    """test"""
    assert solution.jump_the_five("123-456-7890") == "987-604-3215"


# --------------------------------------------------
@pytest.mark.parametrize(
    "solution", [solution1, solution2, solution3, solution4, solution5]
)
def test_02(solution):
    """test"""
    assert (
        solution.jump_the_five("That number to call is 098-765-4321.")
        == "That number to call is 512-340-6789."
    )
