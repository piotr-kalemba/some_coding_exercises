from random import randint


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def selection_sort(a):
    for i in range(len(a) - 1):
        swap(a, i, i + a[i:].index(min(a[i:])))


def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key


def partition(a, start, end):
    r = randint(start, end)
    swap(a, r, end)
    pivot = a[end]
    first = start
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, first)
            first += 1
    swap(a, first, end)
    return first


def quick(a, start, end):
    if end - start > 0:
        p = partition(a, start, end)
        quick(a, start, p-1)
        quick(a, p+1, end)


def quick_sort(a):
    quick(a, 0, len(a) - 1)


def merge(a, b, start, middle, stop):
    left = start
    right = middle
    for i in range(start, stop):
        if right == stop or (left < middle and a[left] <= a[right]):
            b[i] = a[left]
            left += 1
        else:
            b[i] = a[right]
            right += 1
    for i in range(start, stop):
        a[i] = b[i]


def merge_recursively(a, b, start, stop):
    if stop - start > 1:
        middle = (stop + start) // 2
        merge_recursively(a, b, start, middle)
        merge_recursively(a, b, middle, stop)
        merge(a, b, start, middle, stop)


def merge_sort(a):
    b = [0] * len(a)
    merge_recursively(a, b, 0, len(a))


def create_equal(a, m):
    return [a.count(i) for i in range(m)]


def create_next(equal, m):
    return [sum(equal[:value]) for value in range(m)]


def count_sort(a, m):
    result = [0] * len(a)
    equal = create_equal(a, m)
    next = create_next(equal, m)
    for i in range(len(a)):
        value = a[i]
        index = next[value]
        result[index] = a[i]
        next[value] += 1
    return result
