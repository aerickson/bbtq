import os
import subprocess

import pytest


@pytest.fixture
# script working directory
def root_dir():
    swd = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(swd, "../.."))


def test_lvl0(root_dir):
    command = "poetry run tq %s/bbtq/tests/simple.toml ." % (root_dir)
    print(command)
    result = subprocess.run(command, shell=True, capture_output=True)
    expected = 'title = "TOML Example 2345"'
    assert result.stdout.decode().strip() == expected


def test_lvl1(root_dir):
    command = "poetry run tq %s/bbtq/tests/test.toml .title" % (root_dir)
    result = subprocess.run(command, shell=True, capture_output=True)
    expected = "TOML Example"
    assert result.stdout.decode().strip() == expected


def test_lvl2(root_dir):
    command = "poetry run tq %s/bbtq/tests/test.toml .database.ports" % (root_dir)
    result = subprocess.run(command, shell=True, capture_output=True)
    expected = "[8001, 8001, 8002]"
    assert result.stdout.decode().strip() == expected


def test_deep(root_dir):
    # tq .fruit.apple.color test/deep.toml
    command = "poetry run tq %s/bbtq/tests/deep.toml .fruit.apple.color" % (root_dir,)
    result = subprocess.run(command, shell=True, capture_output=True)
    expected = "red"
    assert result.stdout.decode().strip() == expected


def test_array_access(root_dir):
    # tq .fruit.apple.color test/deep.toml
    command = "poetry run tq %s/bbtq/tests/deep.toml '.this.ports[1]'" % (root_dir,)
    result = subprocess.run(command, shell=True, capture_output=True)
    expected = "8001"
    assert result.stdout.decode().strip() == expected
