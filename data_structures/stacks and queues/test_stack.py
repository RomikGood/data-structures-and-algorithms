from .stack import Stack

def small_stack():
    stack = Stack()
    stack.push(1)
    stack.push(1)
    stack.push(1)
    stack.push(1)
    return stack


def test_stack_class_exists():
    assert Stack