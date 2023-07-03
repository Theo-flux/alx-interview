#!/usr/bin/python3
from math import factorial


def pascal_triangle(num):
    a = []

    if num < 0:
        return a

    for n in range(num):
        e = []
        for r in range(n+1):
            e.append(factorial(n)//(factorial(n-r)*factorial(r)))
        a.append(e)
    return a
