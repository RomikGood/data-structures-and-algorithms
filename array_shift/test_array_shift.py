from .array_shift import insert_shift_array
import pytest

def test_even_insert_array():
    expected = [1,2,5,3,4]
    actual = insert_shift_array([1,2,3,4], 5)
    assert expected == actual

def test_odd_insert_array():
    expected = [1,2,3,6,4,5]
    actual = insert_shift_array([1,2,3,4,5], 6)
    assert expected == actual

def test_insert_shift_array_exists():
    assert insert_shift_array