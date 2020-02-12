import numpy as np

a = np.arange(1, 50, 1, int)
a = a.reshape(7,7)

def rec_rotate(a):
    """recursive version of rotating a square matrix in place by 90 degrees"""
    n = len(a) - 1
    if n < 2:
        return True
    a[0, 0], a[0, -1] = a[0, -1], a[0, 0]
    a[-1, -1], a[-1, 0] = a[-1, 0], a[-1, -1]
    for i in range(1, n):
        a[0, i], a[i, -1] = a[i, -1], a[0, i]
    for i in range(1, n):
        a[0, i], a[-1, i] = a[-1, i], a[0, i]
    for i in range(1, n):
        a[0, i], a[i, 0] = a[i, 0], a[0, i]
    rec_rotate(a[1:-1, 1:-1])


def rotate_sides(a, k, n):
    a[k, k], a[k, n-k] = a[k, n-k], a[k, k]
    a[n-k, n-k], a[n-k, k] = a[n-k, k], a[n-k, n-k]
    for i in range(k+1, n-k):
        a[k, i], a[i, n-k] = a[i, n-k], a[k, i]
    for i in range(k+1, n-k):
        a[k, i], a[n-k, i] = a[n-k, i], a[k, i]
    for i in range(k+1, n-k):
        a[k, i], a[i, k] = a[i, k], a[k, i]


def rotate_in_place(a):
    """iterative version of the recursive algorithm"""
    k = 0
    n = len(a) - 1
    while k < n:
        rotate_sides(a, k, n)
        k += 1
        n -= 1

print(a)
for _ in range(4):
    rec_rotate(a)
print(a)