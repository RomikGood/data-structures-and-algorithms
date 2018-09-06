class Queue(object):
    """difining queue for traversal
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


class BinaryTree:

    def __init__(self, iterable=None):
        self.root = None
        if iterable is None:
            iterable = []
        for value in iterable:
            self.insert(value)

    def insert(self, value):
        if(self.root is None):
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curNode):
        if(curNode.value > value):
            if(curNode.left is None):
                curNode.left = Node(value)
            else:
                self._insert(value, curNode.left)
        else:
            if(curNode.right is None):
                curNode.right = Node(value)
            else:
                self._insert(value, curNode.right)

    def BFT(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = []
        while len(queue) > 0:
            queue.peek()
            traversal.append(queue.peek())
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
            
    def find_max(self, start):
        max = self.BFT(start)[0]
        for item in self.BFT(start):
            if item > max:
                max = item
        return max

# tree = BinaryTree([7, 7, 16, 7, 3, 64])


# print(tree.BFT(tree.root))
# print(tree.find_max(tree.root))
