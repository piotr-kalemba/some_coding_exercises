class Graph:

    def __init__(self, incidence_dict):
        self.graph = incidence_dict

    def vertices(self):
        return self.graph.keys()

    def deg(self, vertex):
        return len(self.graph[vertex])

    def in_deg(self, vertex):
        g = self.graph
        return len([node for node in self.vertices() if vertex in g[node]])