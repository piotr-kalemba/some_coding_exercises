from graph import Graph


def hamil_rec(graph, k, n, c, legal, vertex):
    g = graph.graph
    for v in g[c[k-1]]:
        if k == n and v == vertex:
            print(c)
        else:
            if legal[v]:
                c[k] = v
                legal[v] = False
                hamil_rec(graph, k+1, n, c, legal, vertex)
                legal[v] = True


def hamilton(graph):
    n = len(graph.vertices())
    vertex = graph.vertices()[0]
    legal = {v: True for v in graph.vertices()}
    legal[vertex] = False
    c = [vertex] * (n + 1)
    hamil_rec(graph, 1, n, c, legal, vertex)


if __name__ == '__main__':

    g = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '4', '5'],
        '4': ['1', '3', '5'],
        '5': ['2', '3', '4']
    }
    graph = Graph(g)
    hamilton(graph)




