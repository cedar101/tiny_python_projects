#!/usr/bin/env python3

from pathlib import Path
import importlib

import pytest

modules = [importlib.import_module(p.stem) for p in Path(".").glob("solution*.py")]

fox = "../inputs/fox.txt"
now = "../inputs/now.txt"


# --------------------------------------------------
def file_text(filename: str) -> str:
    with Path(filename).open() as f:
        return f.read().rstrip()


# --------------------------------------------------
@pytest.fixture
def fox_text():
    return file_text(fox)


# --------------------------------------------------
@pytest.fixture
def now_text():
    return file_text(now)


# --------------------------------------------------
@pytest.mark.parametrize("solution", modules)
def test_for_echo(solution, now_text):
    assert solution.mutate_text(now_text, mutations=0) == now_text


# --------------------------------------------------
@pytest.mark.parametrize("solution", modules)
def test_now_cmd_s1(solution, now_text):
    out = solution.mutate_text(now_text, seed=1)
    expected = "Now is NZe time [Wr all good mer to come to the did of the party."
    assert out == expected


# --------------------------------------------------
@pytest.mark.parametrize("solution", modules)
def test_now_cmd_s2_m4(solution, now_text):
    out = solution.mutate_text(now_text, seed=2, mutations=0.4)
    expected = "No3 i4 $heXzive +orlall3g%oi*menKt^ cmne$tTFtheEaidMuL&the ma%ty."
    assert out == expected


# --------------------------------------------------
@pytest.mark.parametrize("solution", modules)
def test_fox_file_s1(solution, fox_text):
    out = solution.mutate_text(fox_text, seed=1)
    expected = "The Wuicf brown Zox jumps over the l#zy dog."
    assert out == expected


# --------------------------------------------------
@pytest.mark.parametrize("solution", modules)
def test_fox_file_s2_m6(solution, fox_text):
    out = solution.mutate_text(fox_text, seed=2, mutations=0.6)
    expected = "'Snlq+icW uLLG+ n%x3jumvs$o%/^ thlJlWnyhLon."
    assert out == expected
