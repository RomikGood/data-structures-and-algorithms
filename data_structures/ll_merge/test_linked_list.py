from .ll_merge import LinkedList, Node

# from node import Node
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(5)
    ll.append(7)
    ll.append(9)
    ll.append(10)
    return ll


@pytest.fixture
def small_list_2():
    ll = LinkedList()
    ll.append(2)
    ll.append(6)
    ll.append(7)
    ll.append(12)
    ll.append(15)
    return ll


def test_first_list(small_list):
    '''Verifies that list exist
    '''
    assert LinkedList


def test_second_list(small_list_2):
    '''Verifies that list exist
    '''
    assert LinkedList
    

def test_first_includes_values(small_list):
    '''test takes firs list as a param and cheches if the data was appended correctly
    '''
    assert small_list.includes(1)
    assert small_list.includes(5)
    assert small_list.includes(15) == False


def test_second_includes_values(small_list_2):
    '''test takes second list as a param and cheches if the data was appended correctly
    '''
    assert small_list_2.includes(2)
    assert small_list_2.includes(15)
    assert small_list_2.includes(1) == False


def test_values_from_second_list_exist_in_first_list(small_list, small_list_2):
    '''this test ferifies that data from second list was merge to the first list
    '''
    small_list.merge_sorted(small_list_2)
    assert small_list.includes(15)
    assert small_list.includes(2)
