from .node import Node


class Stack(object):
    def __init__(self):
        self.head = None

    def __len__(self):
        return self.length

    def __str__(self):
        return f'stack top: {self.head.value}  | stack Length: {len(self)}'

    def push(self, value) -> None:
        self.head = Node(value, self.head)

    def pop(self):
        if self.head is None:
            raise EmptyStackException("Pop from empty stack.")

        value = self.head.value
        self.head = self.head.next

        return value

    def peek(self) -> int:
        if self.head is None:
            raise EmptyStackException("Peek from empty stack.")

        return self.head.value

    def is_empty(self) -> bool:
        return self.head is None


class EmptyStackException(Exception):
    pass
