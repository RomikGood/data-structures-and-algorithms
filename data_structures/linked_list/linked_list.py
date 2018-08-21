from .node import Node
# from typing import Any


class LinkedList(object):
    def __init__(self, iterable=None):
        self.head = None
        self._length: int = 0
        if iterable is None:
            iterable = []
        for value in iterable:
            self.insert(value)

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length


    def insert(self, val):
        self.head = Node(val, self.head)
        self._length += 1

    def includes(self, val) -> bool:
        current = self.head

        while current:
            if current.val == val:
                return True
            current = current._next
        return False

    def append(self, val):
        current = self.head
        while current._next:
            current = current._next
        new_node = Node(val)
        current._next = new_node
        self._length += 1

    def add_before(self, targetValue, value):
        newNode = Node(value)
        node = self.head
        if node.val == targetValue:
            newNode._next = self.head
            self.head = newNode

        while node._next is not None:
            if node._next.val == targetValue:
                newNode._next = node._next
                node._next = newNode
                return
            else:
                node = node._next

    def add_after(self, targetValue, value):
        newNode = Node(value)
        node = self.head
        while node._next is not None:
            if node.val == targetValue:
                newNode._next = node._next
                node._next = newNode
                return
            else:
                node = node._next
        if node.val == targetValue:
            newNode._next = None
            node.val = newNode
        
