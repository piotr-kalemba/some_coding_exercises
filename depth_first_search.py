from graph import Graph


def depth_rec(graph, vertex, visited, new):
    g = graph.graph
    new[vertex] = False
    visited.append(vertex)
    for vert in g[vertex]:
        if new[vert]:
            depth_rec(graph, vert, visited, new)


def depth_search(graph, vertex):
    g = graph.graph
    visited = [vertex]
    stack = []
    new = {v: True for v in graph.vertices()}
    new[vertex] = False
    stack.append(vertex)
    while stack:
        v = stack.pop()
        for u in g[v]:
            if new[u]:
                new[u] = False
                stack.append(u)
                visited.append(u)
    return visited


g = {
    '1': ['2', '4', '12'],
    '2': ['1', '4'],
    '3': ['7'],
    '4': ['1', '2', '6', '7', '12'],
    '5': ['6', '8', '9'],
    '6': ['4', '5', '7', '13'],
    '7': ['3', '4', '6'],
    '8': ['5', '9'],
    '9': ['5', '6', '8'],
    '10': ['11', '12'],
    '11': ['10', '12'],
    '12': ['1', '4', '10', '11'],
    '13': ['6']
}

graph = Graph(g)
visited = []
new = {vert: True for vert in graph.vertices()}
depth_rec(graph, '1', visited, new)
print(visited)

result = depth_search(graph, '1')
print(result)