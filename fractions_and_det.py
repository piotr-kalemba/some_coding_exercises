from functools import reduce
import numpy as np


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


class Fraction:

    def __init__(self, numerator, denominator):
        common_factor = gcd(numerator, denominator)
        if denominator == 0:
            raise ZeroDivisionError
        else:
            self.denominator = denominator
        self.numerator = int(numerator / common_factor)
        self.denominator = int(denominator / common_factor)

    def __add__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.numerator
        return Fraction(numerator, denominator)

    def inverse(self):
        if self.numerator == 0:
            raise ZeroDivisionError
        return Fraction(self.denominator, self.numerator)

    def opp_inv(self):
        return self.inverse() * (-1)

    def is_zero(self):
        return self.numerator == 0

    def __str__(self):
        if self.denominator == 1:
            return f'{self.numerator}'
        return f'{self.numerator} / {self.denominator}'


def swap_raws(a, i, j):
    v = a[i, :].copy()
    a[i, :] = a[j, :]
    a[j, :] = v


def find_non_zero(a, i, n):
    j = 0
    while i + j < n and a[i + j, i].is_zero():
        j += 1
    if i + j == n:
        return -1
    return i + j


def det_frac(a):
    n = a.shape[0]
    sign = 1
    for i in range(n):
        j = find_non_zero(a, i, n)
        if j == -1:
            return Fraction(0, 1)
        if j > i:
            swap_raws(a, i, j)
            sign = -sign
        for k in range(i + 1, n):
            if not a[k, i].is_zero():
                a[k, :] = a[k, :] + a[i, :] * (a[k, i] * a[i, i].opp_inv())
    return reduce(lambda x, y: x * y, np.diag(a)) * sign


def show_array(a):
    s = a.copy()
    for i in range(s.shape[0]):
        s[i, :] = [str(item) for item in a[i, :]]
    print(s)


a = np.array(
    [Fraction(0, 1), Fraction(1, 2), Fraction(2, 1), Fraction(0, 1), Fraction(1, 1), Fraction(3, 2), Fraction(-1, 1),
     Fraction(1, 1), Fraction(2, 1), Fraction(1, 1), Fraction(6, 1), Fraction(0, 1), Fraction(0, 1),
     Fraction(1, 1), Fraction(-1, 1), Fraction(1, 3)])
a = a.reshape((4,4))
show_array(a)
f = det_frac(a)
print(f)

