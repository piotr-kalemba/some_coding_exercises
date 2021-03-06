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

    def __iadd__(self, other):
        return other.__add__(self)

    def __mul__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.numerator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        return -other + self

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError
        return self * other.inverse()

    def __neg__(self):
        return self * (-1)

    def inverse(self):
        if self.numerator == 0:
            raise ZeroDivisionError
        return Fraction(self.denominator, self.numerator)

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other):
        return not self.__eq__(other)

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


def det(a):
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
                a[k, :] = a[k, :] + a[i, :] * (a[k, i] / -a[i, i])
    return reduce(lambda x, y: x * y, np.diag(a)) * sign


def show_array(a):
    s = a.copy()
    for i in range(s.shape[0]):
        s[i, :] = [str(item) for item in a[i, :]]
    print(s)


def inserted_column(a, i, v):
    c = a.copy()
    c[:, i] = v
    return c


def find_solutions(equations):
    n = equations.shape[0]
    a = equations[:, :-1]
    b = equations[:, -1]
    if det(a).is_zero():
        print('The system is either inconsistent or has no unique solution.')
        return None
    denominator = det(a).inverse()
    return np.array([det(inserted_column(a, i, b)) * denominator for i in range(n)])


def multiply(a, v):
    return [reduce(lambda x, y: x + y, row * v) for row in a]


def check_solutions(equations, solutions):
    for index, value in enumerate(multiply(equations[:, :-1], solutions), 0):
        if value != equations[index, -1]:
            return False
    return True

equations = np.array(
    [Fraction(0, 1), Fraction(1, 2), Fraction(2, 1), Fraction(0, 1), Fraction(1, 2),
     Fraction(1, 1), Fraction(3, 2), Fraction(-1, 1), Fraction(1, 1), Fraction(2, 3),
     Fraction(2, 1), Fraction(1, 1), Fraction(6, 1), Fraction(0, 1), Fraction(3, 4),
     Fraction(0, 1), Fraction(1, 1), Fraction(-1, 1), Fraction(1, 3), Fraction(2, 1)])
equations = equations.reshape((4,5))


def solve_system(equations):
    solutions = find_solutions(equations)
    for i in range(equations.shape[0]):
        print(f'x[{i}] = {solutions[i]}')


solutions = find_solutions(equations)
solve_system(equations)
answer = check_solutions(equations, solutions)

if answer:
    print("The solutions are valid!")
else:
    print("The solutions are invalid!")
