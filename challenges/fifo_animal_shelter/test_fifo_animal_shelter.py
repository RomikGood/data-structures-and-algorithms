from .fifo_animal_shelter import AnimalShelter
import pytest


@pytest.fixture
def empty_queue():
    return AnimalShelter()


@pytest.fixture
def small_queue():
    queue = AnimalShelter()
    queue.enqueue('cat')
    queue.enqueue('cat')
    queue.enqueue('dog')
    queue.enqueue('cat')
    return queue


def test_QueueWithStacks_class_exists():
    '''class AnimalShelter exists
    '''
    assert AnimalShelter


def test_can_instantiate_empty_queue(empty_queue):
    '''test if empty queue exists
    '''
    assert isinstance(empty_queue, AnimalShelter)


def test_if_dequeue_removes_correct_animals(small_queue):
    """funtion verify that dequeue method removes right animal
    """
    assert small_queue.dequeue('cat') == 'cat'
    assert small_queue.dequeue('dog') == 'dog'


def test_if_queue_dequeue_removes_items(small_queue):
    """funtion verify that dequeue methods removes correct value from hte list
    """
    small_queue.dequeue('cat')
    assert small_queue.size() == 3
    small_queue.dequeue('dog')
    assert small_queue.size() == 2


def test_if_queue_dequeue_(small_queue):
    """funtion verify that dequeue methods work with one value
    """
    small_queue.dequeue('pref')
    assert small_queue.get() == ['dog', 'cat', 'cat']
