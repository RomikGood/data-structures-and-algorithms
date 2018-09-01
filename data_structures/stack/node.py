class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f'{self.val}'
  
    def __repr__(self):
        return f'<Node | Val: {self.val} | Next: {self._next}>'