import os

import btq
import pytest
import toml


def test_basic():
  toml_object = toml.loads("[car]\nname = 'fun car'")
  result = btq.filter_toml(toml_object, ".car.name")
  expected = "fun car"
  assert result == expected

def test_filter_exceptions():
  with pytest.raises(btq.core.BTQInvalidKeyException):
    toml_object = toml.loads("[car]\nname = 'fun car'")
    result = btq.filter_toml(toml_object, ".car.zzz")

def test_main_exception_bad_file():
  with pytest.raises(FileNotFoundError):
    btq.main('bad_path', 'test_filter')
