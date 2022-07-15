import pytest
import toml

import bbtq


def test_basic():
    toml_object = toml.loads("[car]\nname = 'fun car'")
    result = bbtq.filter_toml(toml_object, ".car.name")
    expected = "fun car"
    assert result == expected


def test_filter_exceptions_1():
    with pytest.raises(bbtq.BTQInvalidKeyException):
        toml_object = toml.loads("[car]\nname = 'fun car'")
        bbtq.filter_toml(toml_object, ".car.zzz")


def test_filter_exceptions_2():
    with pytest.raises(bbtq.BTQInvalidIndexException):
        toml_object = toml.loads("[car]\nname = [1,2,3]")
        bbtq.filter_toml(toml_object, ".car.name[7]")


def test_filter_exceptions_3():
    with pytest.raises(bbtq.BTQInvaildArrayFilterException):
        toml_object = toml.loads("[car]\nname = [1,2,3]")
        bbtq.filter_toml(toml_object, ".car.name[string]")


def test_main_exception_bad_file():
    with pytest.raises(FileNotFoundError):
        bbtq.main("bad_path", "test_filter")


# check main's handling of exceptions
def test_main_exception():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        bbtq.main("./bbtq/tests/deep.toml", ".fruit.apple.color.peach")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1
