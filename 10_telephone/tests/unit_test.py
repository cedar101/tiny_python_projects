#!/usr/bin/env python3
"""tests for picnic.py"""

import pytest
from pathlib import Path
import importlib

# import solution1, solution2, solution3, solution4, solution5


modules = [importlib.import_module(p.stem) for p in Path(".").glob("solution*.py")]


# --------------------------------------------------
@pytest.mark.parametrize("solution", modules)
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "The quick brown fox jumps over the lazy dog.",
            "The quick brown fox jumps over the lazy dog.",
        ),
    ],
)
def test_for_echo(prg, now_text):
    out = check_output([prg, "-m", "0", now_text], text=True)
    assert out.rstrip() == f'You said: "{now_text}"\nI heard : "{now_text}"'


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_now_cmd_s1(prg, now_text):
    out = check_output([prg, "-s", "1", now_text], text=True)
    expected = "Now is NZe time [Wr all good mer to come to the did of the party."
    assert out.rstrip() == f'You said: "{now_text}"\nI heard : "{expected}"'


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_now_cmd_s2_m4(prg, now_text):
    out = check_output([prg, "-s", "2", "-m", ".4", now_text], text=True)
    expected = "No3 i4 $heXzive +orlall3g%oi*menKt^ cmne$tTFtheEaidMuL&the ma%ty."
    assert out.rstrip() == f'You said: "{now_text}"\nI heard : "{expected}"'


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_fox_file_s1(prg, fox_text):
    out = check_output([prg, "--seed", "1", fox_text], text=True)
    expected = "The Wuicf brown Zox jumps over the l#zy dog."
    assert out.rstrip() == f'You said: "{fox_text}"\nI heard : "{expected}"'


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_fox_file_s2_m6(prg, fox_text):
    out = check_output([prg, "--seed", "2", "--mutations", ".6", fox_text], text=True)
    expected = "'Snlq+icW uLLG+ n%x3jumvs$o%/^ thlJlWnyhLon."
    assert out.rstrip() == f'You said: "{fox_text}"\nI heard : "{expected}"'
