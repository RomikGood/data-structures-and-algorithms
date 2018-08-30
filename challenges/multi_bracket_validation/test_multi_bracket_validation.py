from .multi_bracket_validation import multi_bracket_validation
import pytest


@pytest.fixture
def small_string():
    multi_bracket_validation('')


def test_if_function_return_False(small_string):
    """funtion verify that i terurns False
    """
    assert multi_bracket_validation('(') is False
    