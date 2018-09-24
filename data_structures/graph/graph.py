class Graph:
    def __init__(self):
        self.graph = {}
        self.edge = []
        self.weight = {}

    def __repr__(self):
        return list(self.graph.keys())

    def __str__(self):
        return list(self.graph.keys())

    def __len__(self):
        return len(list(self.graph.keys()))

    def add_vert(self, val):
        """if val is not it self.graph dict add key 'val' with 
            empty list to the dict
        """
        if val not in self.graph:
            self.graph[val] = []
        else:
            raise ValueError


    
    def has_vert(self, val):
        """function checks if val in graph dict
        """
        if val in self.graph:
            return True
        else:
            return False
        

    def add_edge(self, v1, v2, weight):
        """add weight to our weight dictionary
        """
        if v1 in self.graph and v2 in self.graph:
            self.weight[(v1, v2)] = weight
        else:
            raise ValueError

        # add a relationship and weight between two verts
        # don't forget to validate

    def get_neighbors(self, val):
        """returns list with adjacent vert
        """
        return self.graph[val]
        # Given a val (key), return all all adjacent verts