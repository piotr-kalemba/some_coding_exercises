import numpy as np


def translate_det(seq, rules):
    result = ''
    for char in seq:
        result += rules[char]
    return result


def L_deterministic_generator(start, rules):
    seq = start
    while True:
        yield seq
        seq = translate_det(seq, rules)


def translate_rand(seq, rules):
    result = ''
    for char in seq:
        seqs, weights = zip(*rules[char])
        weights = np.array(weights, dtype=float)
        weights /= sum(weights)
        seq = np.random.choice(seqs, p=weights)
        result += seq
    return result

def L_random_generator(start, rules):
    seq = start
    while True:
        yield seq
        seq = translate_rand(seq, rules)

rules = {
    'A': [('A', 2), ('AB', 1), ('BA', 1)],
    'B': [('AB', 1), ('C', 1)],
    'C': [('A', 1), ('B', 1), ('C', 1)],
}

start = 'A'

generator = L_random_generator(start, rules)

for _ in range(10):
    seq = next(generator)
    print(seq)