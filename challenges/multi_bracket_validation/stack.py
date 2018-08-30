class Node:
    def __init__(self, value):
        self.data = value
        self.front = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        self.length += 1

        if self.head is not None:
            new_node.front = self.head
        self.head = new_node

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def pop(self):
        if not self.is_empty():
            self.length -= 1
            temp = self.head.data
            self.head = self.head.front
            return temp
        else:
            print("can not pop items from an empty list")

    def peek(self):
        return self.head.data

    def length(self):
        return self.length


