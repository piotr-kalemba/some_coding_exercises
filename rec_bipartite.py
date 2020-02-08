from graph import Graph

def rec_partition(graph, root, partition):
    g = graph.graph
    for vertex in g[root]:
        if vertex in partition and partition[vertex] == partition[root]:
            return None
        if vertex not in partition:
            partition[vertex] = 1 - partition[root]
            rec_partition(graph, vertex, partition)
    return partition


def  get_partition(graph, start):
    partition = {start: 0}
    if rec_partition(graph, start, partition) is None:
        return None
    return {v for v in partition if partition[v] == 0}, {v for v in partition if partition[v] == 1}


def get_bi(graph):
    part_0 = set()
    part_1 = set()
    visited = set()
    vertices = set(graph.vertices())
    while len(visited) < len(vertices):
        vertex = (vertices - visited).pop()
        res = get_partition(graph, vertex)
        if res is None:
            return None
        p_0, p_1 = res
        part_0 |= p_0
        part_1 |= p_1
        visited = part_0 | part_1
    return part_0, part_1


def bipartite(graph):
    partition = get_bi(graph)
    if partition is None:
        print('Given graph is not bipartite!')
    else:
        p_0, p_1 = partition
        print('Graph bipartition: ({}, {})'.format(p_0, p_1))


if __name__ == '__main__':
    g = {
    '1': ['a'],
    '2': ['a', 'b'],
    '3': ['c', 'd'],
    '4': ['b'],
    '5': ['a', 'd'],
    '6': ['x', 'y'],
    '7': ['x'],
    'a': ['1', '2', '5'],
    'b': ['2', '4'],
    'c': ['3'],
    'd': ['3', '5'],
    'x': ['6', '7'],
    'y': ['6'],
    'z': [],
    }
    graph = Graph(g)
    bipartite(graph)