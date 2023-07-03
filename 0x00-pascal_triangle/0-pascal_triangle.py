#!/usr/bin/python3
"""
0-pascal's triangle
"""
from math import factorial


def pascal_triangle(num):
    """
    that returns a list of lists of
    integers representing the Pascal’s
    triangle of n

    Args:
        num (int): the length of the list

    Returns:
        list: a list of list of integers
    """
    a = []

    if num < 0:
        return a

    for n in range(num):
        e = []
        for r in range(n+1):
            e.append(factorial(n)//(factorial(n-r)*factorial(r)))
        a.append(e)
    return a
