from .find_maximum_value_binary_tree import BinaryTree, Node
import pytest


@pytest.fixture
def small_tree():
    tree = BinaryTree([5, 33, 7, 1, 3, 64])
    return tree

@pytest.fixture
def neg_tree():
    tree = BinaryTree([-4, -1, -14])
    return tree


def test_bst_exists():
    '''test verifies that BinaryTree class exists
    '''
    assert BinaryTree


def test_if_root_has_correct_value(small_tree):
    '''check for correct value of the root
    '''
    assert small_tree.root.value == 5


def test_breadth_fist_travers_correctly(small_tree):
    '''test verifies that breadth fist traversal outpust correct item
    '''
    actual = [5, 1, 33, 3, 7, 64]
    expected = small_tree.BFT(small_tree.root)
    assert expected == actual


def test_breadth_fist_works_duplicate_value(small_tree):
    '''test verifies that breadth fist traversal outpust correct item
    '''
    actual = [7, 3, 7, 16, 7, 64]
    tree = BinaryTree([7, 7, 16, 7, 3, 64])
    expected = tree.BFT(tree.root)
    assert expected == actual


def test_tree_returns_max_value(small_tree):
    '''test verifies that expected value is a max
    '''
    assert small_tree.find_max(small_tree.root) == 64


def test_tree_returns_max_value_with_negatives(neg_tree):
    ''' test verifies that find outputs correc  max
        value when inputs are negagtive values
    '''
    assert neg_tree.find_max(neg_tree.root) == -1



