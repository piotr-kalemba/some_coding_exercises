from graph import Graph


def find_partition(graph, vertex):
    g = graph.graph
    color = {v: None for v in graph.vertices()}
    color[vertex] = 0
    stack = [vertex]
    visited = [vertex]
    while stack:
        top = stack.pop()
        for v in g[top]:
            if color[v] is None:
                color[v] = 1 - color[top]
                stack.append(v)
                visited.append(v)
            elif color[v] == color[top]:
                return None
    return {v for v in visited if color[v] == 0}, {v for v in visited if color[v] == 1}


def bipartite_graph(graph):
    vertices = set(graph.vertices())
    part_1 = set()
    part_2 = set()
    while vertices:
        vertex = vertices.pop()
        if find_partition(graph, vertex) is None:
            print("The graph is not bipartite!")
            return None
        else:
            s_1, s_2 = find_partition(graph, vertex)
            part_1 |= s_1
            part_2 |= s_2
            vertices -= (s_1 | s_2)
    return part_1, part_2


if __name__ == '__main__':
    g = {
        '1': ['a'],
        '2': ['a', 'b'],
        '3': ['c', 'd'],
        '4': ['b'],
        '5': ['a', 'd'],
        'a': ['1', '2', '5'],
        'b': ['2', '4'],
        'c': ['3'],
        'd': ['3', '5'],
    }
    graph = Graph(g)
    p, q = bipartite_graph(graph)
    print(p,',', q)