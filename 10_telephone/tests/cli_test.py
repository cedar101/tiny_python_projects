#!/usr/bin/env python3
"""tests for telephone.py"""

import random
import string
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT

import pytest


programs = [f"./{p}" for p in Path(".").glob("solution*.py")]
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
@pytest.fixture(name="bad")
def random_string():
    """generate a random filename"""

    return "".join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_exists(prg):
    """exists"""
    assert Path(prg).is_file()


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
@pytest.mark.parametrize("flag", ["-h", "--help"])
def test_usage(prg, flag):
    """usage"""
    out = check_output([prg, flag])
    assert b"usage" in out.lower()


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_bad_seed_str(prg, bad):
    """bad seed str value"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-s", bad, fox], text=True, stderr=STDOUT)
    assert "usage" in excinfo.value.stdout.lower()
    assert f"invalid int value: '{bad}'" in excinfo.value.stdout


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_bad_mutation_str(prg, bad):
    """bad mutation str value"""

    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-m", bad, fox], text=True, stderr=STDOUT)
    assert "usage" in excinfo.value.stdout.lower()
    assert f"invalid float value: '{bad}'" in excinfo.value.stdout


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
@pytest.mark.parametrize("val", ["-1.0", "10.0"])
def test_bad_mutation(prg, val):
    """bad mutation values"""

    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-m", val, fox], text=True, stderr=STDOUT)

    assert "usage" in excinfo.value.stdout.lower()
    assert f'--mutations "{val}" must be between 0 and 1' in excinfo.value.stdout


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
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
