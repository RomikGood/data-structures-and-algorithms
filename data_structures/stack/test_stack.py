from .stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def small_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


def test_stack_class_exists():
    assert Stack


def test_can_instantiate_empty_stack(empty_stack):
    '''test if empty tack exist
    '''
    assert isinstance(empty_stack, Stack)


def test_if_stack_pops_items_fromt_the_top(small_stack):
    """funtion verify that pop method return item from the top
    """
    assert small_stack.pop() == 4
    assert small_stack.pop() == 3


def test_if_stack_push_and_pop_one_item(empty_stack):
    """funtion verify that push and pop methods work with one value
    """
    empty_stack.push(1)
    assert empty_stack.pop() == 1
    

def test_if_stack_push_and_peek_one_item(empty_stack):
    """funtion verify that push and peek methods work with one value
    """
    empty_stack.push(1)
    assert empty_stack.peek() == 1
