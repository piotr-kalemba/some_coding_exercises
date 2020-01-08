from depth_first_search import ret_graph


def breadth_search(graph, vertex):
    g = graph.graph
    new = {v: True for v in graph.vertices()}
    pred = {v: None for v in graph.vertices()}
    queue = [vertex]
    new[vertex] = False
    while queue:
        v = queue.pop(0)
        for u in g[v]:
            if new[u]:
                new[u] = False
                queue.append(u)
                pred[u] = v
    return pred


def find_path(graph, v, u):
    pred = breadth_search(graph, v)
    vertex = u
    path = []
    while vertex:
        path.append(vertex)
        vertex = pred[vertex]
    path.reverse()
    return path


graph = ret_graph()
path = find_path(graph, '3', '10')
print(path)