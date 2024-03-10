#!/usr/bin/env python3
"""tests for hello.py"""

import os
from subprocess import check_output

prg = "./hello.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_runnable():
    """Runs using python3"""

    out = check_output(["python3", prg])
    assert out.strip() == b"Hello, World!"


# --------------------------------------------------
def test_executable():
    """Says 'Hello, World!' by default"""

    out = check_output([prg])
    assert out.strip() == b"Hello, World!"


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        out = check_output([prg, flag])
        assert b"usage" in out.lower()


# --------------------------------------------------
def test_input():
    """test for input"""

    for val in ["Universe", "Multiverse"]:
        for option in ["-n", "--name"]:
            out = check_output([prg, option, val], text=True)
            assert out.strip() == f"Hello, {val}!"
