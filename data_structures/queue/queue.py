from .node import Node


class Queue:

    def __init__(self, value=None):
        self.length = 0
        self.front = None
        self.back = None
        if value is not None:
            for data in value:
                self.enqueue(data)

    def __len__(self):
        return self.length

    def __str__(self):
        return f'Queue Front: {self.front.value} | Queue Back: {self.back.value} | Queue Length: {len(self)}'

    def enqueue(self, data):
        if self.back is None:
            self.front = Node(data)
            self.back = self.front
            self.length += 1
        else:

            self.back.next = Node(data)
            self.back = self.back.next
            self.length += 1
 
    def dequeue(self):
        if self.front is None:
            return None
        else:
            to_return = self.front.data
            self.front = self.front.next
            return to_return
