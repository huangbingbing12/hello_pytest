import pytest
def _a():
    print("test_a")
    assert 1()
    print("test_b")

def test_b():
    login()
    assert 0
def login():
    print("login")
    assert 1