class Stack:
    def __init__(self):
        self.top = None
        self._length = 0


def __repr__(self):
    pass


def __str__(self):
    pass

def (self):
    pass


def _push(self, value):
    '''Method that accepts a value of any type and creates a dew Node in the Stack instance
    
    Args:
        value(object):Any

    Return: Node
    '''
    # node =  Node(value)
    # node._next = self.top
    #  self.top = node
    self.top = Node(value, self.top)
    self._length += 1
    
    return self.top


def pop(self):
    '''
    '''
    tmp = self.top
    self.top = tmp._next
    tmp._next = None # Specificity, though the garbag collector will do this for you.

    self._length -= 1
    return tmp


def peek(self):
    return self.top