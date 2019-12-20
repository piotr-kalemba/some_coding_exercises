import numpy as np


def optimal_allocation(weight, value, vol):
    n = len(weight)
    optimal = np.zeros((n+1, vol+1), dtype=int)
    x = np.zeros((n+1, vol+1), dtype=int)
    y = np.zeros((n+1, vol+1), dtype=int)
    for i in range(1, n+1):
        for j in range(1, vol+1):
            if j >= weight[i-1] and optimal[i-1, j] < optimal[i, j-weight[i-1]] + value[i-1]:
                optimal[i, j] = optimal[i, j-weight[i-1]] + value[i-1]
                x[i, j] = i
                y[i, j] = j-weight[i-1]
            else:
                optimal[i, j] = optimal[i-1, j]
                x[i, j] = i-1
                y[i, j] = j
    return x, y


def pack_knapsack(weight, value, vol):
    x, y = optimal_allocation(weight, value, vol)
    knapsack = []
    i = len(weight)
    j = vol
    while i * j != 0:
        if i == x[i, j]:
            knapsack.append(i - 1)
        i, j = x[i, j], y[i, j]
    knapsack.sort()
    return knapsack


weight = [6, 2, 3, 2, 3, 1]
value = [6, 4, 5, 7, 10, 2]
cap = 23

knapsack = pack_knapsack(weight, value, cap)
print(knapsack)