import random

class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.value = val
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value}'
  
    def __repr__(self):
        return f'<Node | Val: {self.value} | Left: {self.left} | Right: {self.right} >'


class BinaryTree:
    def __init__(self, iterable=None):
    
        self.root = None
        if iterable is None:
            iterable = []
        for item in iterable:
            self.insert(item)

    def __str__(self):
        return f'Root: {self.root}'
        pass

    def __repr__(self):
        return f'<BST | Root: {self.root}>'

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:    
            current = self.root
            while current:
                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    else:
                        current = current.right


    def in_order(self, callable=lambda node: print(node)):
        """Go left, visit, then go right
        """
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left:
                _walk(node.left)

            # Visit
            callable(node)

            # Go right
            if node.right:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """Visit, go left, then right
        """
        def _walk(node=None):
            if node is None:
                return

            # Visit
            callable(node)

            # Go left
            if node.left:
                _walk(node.left)

            # Go right
            if node.right:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """Go left, then right, Visit
        """
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left:
                _walk(node.left)

            # Go right
            if node.right:
                _walk(node.right)

            # Visit
            callable(node)

        _walk(self.root)


# if __name__ == '__main__':
#     tree = BinaryTree()
#     root = None
#     for i in range(10):
#         root = tree.insert(root, random.randint(0,100))
#     tree.in_order(root)