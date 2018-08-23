from .linked_list import LinkedList, Node
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll3 = LinkedList()
    ll3.insert(1)
    ll3.insert(5)
    ll3.insert(3)
    ll3.insert(4)
    return ll3


@pytest.fixture
def smalls_list():
    ll2 = LinkedList()
    ll2.insert(2)
    ll2.insert(6)
    ll2.insert(7)
    ll2.insert(8)
    return ll2


