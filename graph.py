import numpy  as np

class Graph:

    def __init__(self, incidence_list, weights=None):
        self.graph = incidence_list
        if weights:
            self.weights = weights

    def vertices(self):
        return list(self.graph.keys())

    def deg(self, vertex):
        return len(self.graph[vertex])

    def in_deg(self, vertex):
        g = self.graph
        return len([node for node in self.vertices() if vertex in g[node]])

    @classmethod
    def from_array(cls, array, nodes, inf):
        weights = {node: {vertex: array[nodes.index(node)][nodes.index(vertex)] for vertex in nodes} for node in nodes}
        incidence_list = {node: [vertex for vertex in nodes if weights[node][vertex] != inf] for node in nodes}
        return cls(incidence_list, weights)

    def create_array(self, inf):
        g = self.graph
        vertices = self.vertices()
        size = len(vertices)
        array = np.zeros((size, size))
        for k in range(size):
            for l in range(size):
                array[k][l] = self.weights[vertices[k]][vertices[l]] if vertices[l] in g[vertices[k]] else inf
        return array


