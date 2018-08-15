from .array_binary_search import binary_search
import pytest

def test_even_binary_search():
    expected = 2
    actual = binary_search([1,2,3,4], 3)
    assert expected == actual

def test_binary_search():
    expected = 4
    actual = binary_search([1,2,3,4,11], 11)
    assert expected == actual

def test_no_key_exist_binary_search():
    expected = -1
    actual = binary_search([1,2,3,4,11], 5)
    assert expected == actual

def test_binary_search_exists():
    assert binary_search