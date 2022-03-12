import pytest

from my_pkg.math import add, subtract, multiply, divide

def test_always_passes():
    assert True
    
def test_always_fails():
    assert False

def test_add():
    assert add(2, 3) == 5
    
def test_subtract():
    assert subtract(5, 2) == 3
    
def test_multiply():
    assert multiply(2, 4) == 8
    
def test_divide():
    assert divide(8, 2) == 4