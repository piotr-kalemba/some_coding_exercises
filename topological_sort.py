from .graph import Graph


def topological_sort(graph):
    """we assume the graph is acyclic"""
    vertices = graph.vertices()
    g = graph.graph
    in_degree = {vertex: graph.in_deg(vertex) for vertex in vertices}
    stack = [vertex for vertex in vertices if in_degree[vertex] == 0]
    linear_order = []
    while stack:
        vertex = stack.pop()
        linear_order.append(vertex)
        for node in vertices:
            if vertex in g[node]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    stack.append(node)
    return linear_order


