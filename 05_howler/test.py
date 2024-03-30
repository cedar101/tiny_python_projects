#!/usr/bin/env python3
"""tests for howler.py"""

import random
import string
import tempfile
from pathlib import Path
from subprocess import check_output

import pytest


programs = [f"./{p}" for p in Path(".").glob("solution*.py")]


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_exists(prg):
    """exists"""
    assert Path(prg).is_file()


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_usage(prg):
    """usage"""

    for flag in ["-h", "--help"]:
        out = check_output([prg, flag])
        assert b"usage" in out.lower()


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def out_flag():
    """Either -o or --outfile"""

    return random.choice(("-o", "--outfile"))


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_text_stdout(prg):
    """Test STDIN/STDOUT"""

    out = check_output((prg, "foo bar baz"))
    assert out.strip() == b"FOO BAR BAZ"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_text_outfile(prg):
    """Test STDIN/outfile"""

    with tempfile.NamedTemporaryFile("w+") as out_file:
        out = check_output((prg, out_flag(), out_file.name, "foo bar baz"))
        assert not out.strip()
        text = out_file.read().rstrip()
        assert text == "FOO BAR BAZ"


# --------------------------------------------------
@pytest.mark.parametrize("prg", programs)
def test_file(prg):
    """Test file in/out"""

    for expected_file in Path("test-outs").resolve().iterdir():
        with tempfile.NamedTemporaryFile("w+") as out_file:
            basename = expected_file.name
            in_file = expected_file.parent.parent.parent / "inputs" / basename
            out = check_output((prg, out_flag(), out_file.name, str(in_file)))
            assert not out.strip()
            produced = out_file.read().rstrip()
            expected = expected_file.read_text().strip()
            assert expected == produced
