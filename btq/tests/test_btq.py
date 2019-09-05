import os

import btq
import pytest
import toml


def test_basic():
  toml_object = toml.loads("[car]\nname = 'fun car'")
  print(dir(btq))
  result = btq.filter_toml(toml_object, ".car.name")
  expected = "fun car"
  assert result == expected

# def test_exceptions():
#   with pytest.raises(ZeroDivisionError):
#     toml_object = toml.loads("[car]\nname = 'fun car'")
#     result = btq.filter_toml(toml_object, ".car.name..")


# def test_main():
#   pass