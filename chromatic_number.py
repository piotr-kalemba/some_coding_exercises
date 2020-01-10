from graph import Graph


def chrom_rec(graph, p, n, k, color, vert):
    g = graph.graph
    if p == n:
        print(color)
        return True
    for c in range(k):
        if c not in {color[v] for v in g[vert[p]]}:
            color[vert[p]] = c
            return chrom_rec(graph, p+1, n, k, color, vert)


def chromatic_number(graph):
    vert = graph.vertices()
    color = {v: None for v in vert}
    color[vert[0]] = 0
    n = len(vert)
    k = 1
    while not chrom_rec(graph, 1, n, k, color, vert):
        color = {v: None for v in vert}
        color[vert[0]] = 0
        k += 1
    return k

# bipartate graph, so chromatic number = 2
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
G = Graph(g)
r = chromatic_number(G)
print(r)

h = {
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
H = Graph(h)
r = chromatic_number(H)
print(r)



