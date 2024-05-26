#!/usr/bin/env python3
"""tests for abuse.py"""

import random
import string
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT
import logging

import pytest


prg = "./solution.py"  # "./abuse.py"


# --------------------------------------------------
@pytest.fixture(name="bad")
def random_string():
    """generate a random filename"""

    return "".join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """exists"""
    assert Path(prg).is_file()


# --------------------------------------------------
def test_usage():
    """usage"""
    for flag in ["-h", "--help"]:
        out = check_output([prg, flag])
        assert b"usage" in out.lower()


# --------------------------------------------------
def test_bad_adjective_str(bad):
    """bad_adjectives"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-a", bad], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert "invalid int value: '{bad}'" in excinfo.value.stdout


# --------------------------------------------------
def test_bad_adjective_num():
    """bad_adjectives"""

    n = random.choice(range(-10, 0))
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-a", str(n)], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert f'--adjectives "{n}" must be > 0' in excinfo.value.stdout


# --------------------------------------------------
def test_bad_number_str(bad):
    """bad_number"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-n", bad], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert "invalid int value: '{bad}'" in excinfo.value.stdout


# --------------------------------------------------
def test_bad_number_int():
    """bad_number"""

    n = random.choice(range(-10, 0))
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-a", str(n)], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert f'--number "{n}" must be > 0' in excinfo.value.stdout


# --------------------------------------------------
def test_bad_seed(bad):
    """bad seed"""

    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-s", bad], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert f"invalid int value: '{bad}'" in excinfo.value.stdout


# --------------------------------------------------
def test_01():
    """test"""

    out = check_output([prg, "-s", "1", "-n", "1"])
    assert out.strip() == b"You filthsome, cullionly fiend!"


# --------------------------------------------------
def test_02():
    """test"""

    out = check_output([prg, "--seed", "2"])
    expected = b"""
You corrupt, detestable beggar!
You peevish, foolish gull!
You insatiate, heedless worm!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_03():
    """test"""

    out = check_output([prg, "-s", "3", "-n", "5", "-a", "1"])
    expected = b"""
You infected villain!
You vile braggart!
You peevish worm!
You sodden-witted villain!
You cullionly worm!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_04():
    """test"""

    out = check_output([prg, "--seed", "4", "--number", "2", "--adjectives", "4"])
    expected = b"""
You infected, lecherous, dishonest, rotten recreant!
You filthy, detestable, cullionly, base lunatic!
""".strip()
    assert out.strip() == expected
