class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data}'
  
    def __repr__(self):
        return f'<Node | data: {self.data} | Next: {self.next}>'