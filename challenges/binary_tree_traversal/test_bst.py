from .breadth_first_traversal import BinaryTree, Node
import pytest


@pytest.fixture
def small_tree():
    tree = BinaryTree(5)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(11)
    return tree


def test_bst_exists():
    '''test verifies that BinaryTree class exists
    '''
    assert BinaryTree


def test_if_root_has_correct_value(small_tree):
    '''check for correct value of the root
    '''
    assert small_tree.root.value == 5


def test_if_right_child_has_correct_value(small_tree):
    '''test verifies that left child has correct value
    '''
    assert small_tree.root.value == 5
    assert small_tree.root.left.value == 2
    assert small_tree.root.right.value == 3
    assert small_tree.root.left.left.value == 4
    assert small_tree.root.left.right.value == 11


def test_tree_ignores_duplicate_items(small_tree):
    '''test verifies that expected and actual outputs are equal 
    '''
    expected = [5, 2, 3, 4, 11]
    actual = small_tree.BFT(small_tree.root) 
    assert expected == actual

