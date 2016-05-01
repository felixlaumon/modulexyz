import pytest


def test_addition():
    from modulexyz.utils import add
    assert add(1, 2) == 3
