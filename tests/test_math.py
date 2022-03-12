"""Test toy math functions."""

import pytest

from my_pkg.math import add, subtract, multiply, divide


@pytest.mark.unit
def test_add():
    """Test add function."""
    assert add(2, 3) == 5


@pytest.mark.unit
def test_subtract():
    """Test subtract function."""
    assert subtract(5, 2) == 3


@pytest.mark.unit
def test_multiply():
    """Test multiply function."""
    assert multiply(2, 4) == 8


@pytest.mark.unit
def test_divide():
    """Test divide function."""
    assert divide(8, 2) == 4
