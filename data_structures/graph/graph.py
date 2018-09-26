
class Graph:
    def __init__(self):
        self.graph = {}
        self.edge = []
        self.weight = {}

    def __repr__(self):
        return list(self.graph.keys())

    def breadth_first(self):
