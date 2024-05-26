#!/usr/bin/env python3
"""tests for abuse.py"""

import random
import string
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT
from textwrap import dedent
import logging

import pytest


prg = "./solution.py"  # "./abuse.py"


# --------------------------------------------------
@pytest.fixture(name="bad_str")
def random_string() -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
@pytest.fixture(name="bad_num")
def random_negative_integer() -> int:
    return random.randint(-10, 0)


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
def test_bad_adjective_str(bad_str):
    """bad_adjectives"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-a", bad_str], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert f"invalid int value: '{bad_str}'" in excinfo.value.stdout


# --------------------------------------------------
def test_bad_adjective_num(bad_num):
    """bad_adjectives"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-a", str(bad_num)], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert f'--adjectives "{bad_num}" must be > 0' in excinfo.value.stdout


# --------------------------------------------------
def test_bad_number_str(bad_str):
    """bad_number"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-n", bad_str], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert f"invalid int value: '{bad_str}'" in excinfo.value.stdout


# --------------------------------------------------
def test_bad_number_int(bad_num):
    """bad_number"""
    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-n", str(bad_num)], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert f'--number "{bad_num}" must be > 0' in excinfo.value.stdout


# --------------------------------------------------
def test_bad_seed(bad_str):
    """bad seed"""

    with pytest.raises(CalledProcessError) as excinfo:
        check_output([prg, "-s", bad_str], text=True, stderr=STDOUT)
    logging.info(excinfo.value.stdout)
    assert "usage" in excinfo.value.stdout.lower()
    assert f"invalid int value: '{bad_str}'" in excinfo.value.stdout


# --------------------------------------------------
def test_01():
    """test"""

    out = check_output([prg, "-s", "1", "-n", "1"])
    assert out.strip() == b"You filthsome, cullionly fiend!"


# --------------------------------------------------
def test_02():
    """test"""

    out = check_output([prg, "--seed", "2"], text=True)
    expected = dedent(
        """
        You corrupt, detestable beggar!
        You peevish, foolish gull!
        You insatiate, heedless worm!
        """
    ).strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_03():
    """test"""

    out = check_output([prg, "-s", "3", "-n", "5", "-a", "1"], text=True)
    expected = dedent(
        """
        You infected villain!
        You vile braggart!
        You peevish worm!
        You sodden-witted villain!
        You cullionly worm!
        """
    ).strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_04():
    """test"""

    out = check_output(
        [prg, "--seed", "4", "--number", "2", "--adjectives", "4"], text=True
    )
    expected = dedent(
        """
        You infected, lecherous, dishonest, rotten recreant!
        You filthy, detestable, cullionly, base lunatic!
        """
    ).strip()
    assert out.strip() == expected
