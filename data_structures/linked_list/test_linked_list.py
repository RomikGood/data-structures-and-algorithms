from .linked_list import LinkedList, Node
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


def test_linked_list_exists():
    assert LinkedList


def test_create_instance_of_list():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)
   


def test_default_property_head(empty_list):
    assert empty_list.head is None


def test_default_property_length(empty_list):
    assert empty_list._length == 0


def test_insertion_successful(empty_list):
    assert empty_list.head is None
    empty_list.insert(25)
    assert empty_list.head.val == 25
    



def test_length_of_list_increases_on_insertion(empty_list):
    assert len(empty_list) == 0
    empty_list.insert(25)
    assert len(empty_list) == 1


def test_includes_returns_true_if_exists(small_list):
    actual = small_list.includes(4)
    assert actual is True
    assert small_list.includes(1) is True


def test_includes_returns_false_if_not_exists(small_list):
    assert small_list.includes(100) is False
    assert small_list.includes(0) is False


def test_append_has_appended_value(small_list):
    small_list.append(5)
    assert small_list.includes(5) is True


def test_append_has_correct_length(small_list):
    small_list.append(5)
    assert small_list._length == 5


def test_add_before_has_added_value(small_list):
    small_list.add_before(4, 5)
    assert small_list.includes(5)


def test_add_after_has_added_value(small_list):
    small_list.add_after(4, 5)
    assert small_list.includes(5)


def test_add_before_has_correct_length(small_list):
    '''this function tests if output link list has correct length
    '''
    small_list.append(5)
    assert small_list._length == 5
    


def test_add_after_has_correct_length(small_list):
    '''this function tests if output linked list has correct length
    '''
    small_list.append(5)
    assert small_list._length == 5


def test_kth_from_end_return_corrct_value(small_list):
    '''this function tests if function return correct kth value
    '''
    assert small_list.kth_from_end(2) == 3
    assert small_list.kth_from_end(1) == 2


def test_kth_from_end_length_greater_then_value(small_list):
    '''this function tests if argument is greater then the length on link list
    '''
    with pytest.raises(AttributeError):
        small_list.test_kth_from(5)


def test_kth_from_is_zero(small_list):
    '''this function tests if argument is zero from the end
    '''
    with pytest.raises(AttributeError):
        small_list.test_kth_from(0)
