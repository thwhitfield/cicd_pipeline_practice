import pytest

from my_pkg.math import add, subtract, multiply, divide


@pytest.mark.unit
def test_add():
    assert add(2, 3) == 5


@pytest.mark.unit
def test_subtract():
    assert subtract(5, 2) == 3


@pytest.mark.unit
def test_multiply():
    assert multiply(2, 4) == 8


@pytest.mark.unit
def test_divide():
    assert divide(8, 2) == 4
