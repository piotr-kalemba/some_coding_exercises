import numpy as np


def compute_lcs_array(string_1, string_2):
    n = len(string_1)
    m = len(string_2)
    l = np.zeros((n+1, m+1), dtype=int)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if string_1[i-1] == string_2[j-1]:
                l[i, j] = l[i-1, j-1] + 1
            elif l[i-1, j] < l[i, j-1]:
                l[i, j] = l[i, j-1]
            else:
                l[i, j] = l[i-1, j]
    return l


def assemble_lcs(string_1, string_2, l, i, j):
    if i == 0 or j == 0:
        return ""
    if string_1[i-1] == string_2[j-1]:
        return assemble_lcs(string_1, string_2, l, i-1, j-1) + string_1[i-1]
    if l[i, j] == l[i-1, j]:
        return assemble_lcs(string_1, string_2, l, i-1, j)
    return assemble_lcs(string_1, string_2, l, i, j-1)


def find_lcs(string_1, string_2):
    l = compute_lcs_array(string_1, string_2)
    n = len(string_1)
    m = len(string_2)
    return assemble_lcs(string_1, string_2, l, n, m)


string_1 = "CATCGA"
string_2 = "GTACCGTCA"
lcs = find_lcs(string_1, string_2)
print(lcs)