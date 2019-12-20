import numpy as np

class Relation:

    def __init__(self, items, array):
        self.items = items
        self.array = array

    def size(self):
        return len(self.items)

    def rel_tuples(self):
        items = self.items
        array = self.array
        return {(x, y) for x in items for y in items if array[items.index(x)][items.index(y)]}


items = ['a', 'b', 'c']
array = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
])
rel = Relation(items, array)

def trans_cl(rel):
    items = rel.items
    array = rel.array
    n = rel.size()
    a = (array == 1)
    for m in range(n):
        for i in range(n):
            for j in range(n):
                a[i, j] = a[i, j] or (a[i, m] and a[m, j])
    closure = Relation(items, a)
    return closure

print(rel.rel_tuples())
closure = trans_cl(rel)
print(closure.rel_tuples())

