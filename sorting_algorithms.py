from random import randint


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

# selection_sort
def selection_sort(a):
    for i in range(len(a) - 1):
        swap(a, i, i + a[i:].index(min(a[i:])))


# insertion_sort
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key


# quick_sort
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


# merge_sort
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


# count_sort
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


# heap_sort
def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def swap_downwards(a, i, stop):
    to_swap = i
    if left_child(i) < stop and a[i] < a[left_child(i)]:
        to_swap = left_child(i)
    if right_child(i) < stop and a[to_swap] < a[right_child(i)]:
        to_swap = right_child(i)
    if to_swap != i:
        swap(a, i, to_swap)
        return to_swap
    return -1


def bubble_down(a, start, stop):
    to_swap = start
    while to_swap != -1:
        to_swap = swap_downwards(a, to_swap, stop)


def take_apart_heap(heap, stop):
    while stop > 0:
        swap(heap, 0, stop)
        bubble_down(heap, 0, stop)
        stop -= 1


def make_heap(a):
    start = len(a) - 1
    while start >= 0:
        bubble_down(a, start, len(a))
        start -= 1
    return a


def heap_sort(a):
    heap = make_heap(a)
    take_apart_heap(heap, len(heap)-1)


