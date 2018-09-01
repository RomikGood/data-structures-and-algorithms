from .bst import BinaryTree
import pytest


@pytest.fixture
def small_tree():
    bst = BinaryTree([20, 25, 12, 19, 11, 14, 40, 31, 22, 33])
    return bst

@pytest.fixture
def dup_tree():
    bst = BinaryTree([20, 20, 12, 19, 11, 1, 40, 31, 22, 33])
    return bst


def test_bst_exists():
    '''test verifies that BinaryTree class exists
    '''
    assert BinaryTree


def test_if_root_has_correct_value(small_tree):
    assert small_tree.root.value == 20


def test_if_right_child_has_correct_value(small_tree):
    '''test verifies that left child has correct value
    '''
    assert small_tree.root.right.value == 25
    

def test_if_left_child_has_correct_value(small_tree):
    '''test verifies that left child has correct value
    '''
    assert small_tree.root.left.value == 12


def test_tree_ignores_duplicate_items(dup_tree):
    '''test verifies that insert function skips duplicate items
    '''
    assert dup_tree.root.left.value == 12

