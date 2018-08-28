from .queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    return queue


def test_queue_class_exists():
    '''class Queue exist
    '''
    assert Queue


def test_can_instantiate_empty_queue(empty_queue):
    '''test if empty tack exist
    '''
    assert isinstance(empty_queue, Queue)


def test_if_queue_dequeue_items_fromt_the_top(small_queue):
    """funtion verify that dequeue method return item from the buttom
    """
    assert small_queue.dequeue() == 1
    assert small_queue.dequeue() == 2


def test_if_queue_enqueue_and_pop_one_item(empty_queue):
    """funtion verify that enqueue and dequeue methods work with one value
    """
    empty_queue.enqueue(1)
    assert empty_queue.dequeue() == 1
    

def test_if_queue_length_method_works(small_queue):
    """funtion small queue and verifies it's length
    """
    assert len(small_queue) == 4
