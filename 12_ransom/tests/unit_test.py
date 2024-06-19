#!/usr/bin/env python3

from pathlib import Path
import importlib
import random

import pytest

modules = [importlib.import_module(p.stem) for p in Path(".").glob("solution*.py")]


# --------------------------------------------------
@pytest.mark.parametrize("solution", modules)
def test_choose(solution):  # , test_input, expected):
    state = random.getstate()
    random.seed(1)
    choose = solution.choose
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "C"
    assert choose("d") == "d"
    random.setstate(state)
