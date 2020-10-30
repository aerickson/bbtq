import os

import pytest
import toml

import btq

def test_basic():
    toml_object = toml.loads("[car]\nname = 'fun car'")
    result = btq.filter_toml(toml_object, ".car.name")
    expected = "fun car"
    assert result == expected


def test_filter_exceptions_1():
    with pytest.raises(btq.BTQInvalidKeyException):
        toml_object = toml.loads("[car]\nname = 'fun car'")
        _r = btq.filter_toml(toml_object, ".car.zzz")


def test_filter_exceptions_2():
    with pytest.raises(btq.BTQInvalidIndexException):
        toml_object = toml.loads("[car]\nname = [1,2,3]")
        _r = btq.filter_toml(toml_object, ".car.name[7]")


def test_filter_exceptions_3():
    with pytest.raises(btq.BTQInvaildArrayFilterException):
        toml_object = toml.loads("[car]\nname = [1,2,3]")
        _r = btq.filter_toml(toml_object, ".car.name[string]")


def test_main_exception_bad_file():
    with pytest.raises(FileNotFoundError):
        btq.main('bad_path', 'test_filter')


# check main's handling of exceptions
def test_main_exception():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        btq.main('./btq/tests/deep.toml', '.fruit.apple.color.peach')
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1
