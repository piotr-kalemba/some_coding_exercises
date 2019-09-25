from permutation_class import Permutation


def generate_permutations(seq):
    """the function is a recursive generator yielding all permutations of
    the list 'seq' provided the list items are distinct"""
    if len(seq) == 0:
        yield []
    for item in seq:
        i = seq.index(item)
        for sigma in generate_permutations(seq[:i]+seq[i+1:]):
            sigma.insert(0, item)
            yield sigma


def permutations(n):
    """the function generates all permutation objects for all permutations of the elements 0, 1, 2, ... up to n-1"""
    seq = list(range(n))
    for sigma in generate_permutations(seq):
        yield Permutation(sigma)


def print_permutations(n):
    for index, sigma in enumerate(permutations(n), 1):
        print(f'Sigma {index}:\n{sigma}')
