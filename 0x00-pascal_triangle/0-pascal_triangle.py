#!/usr/bin/python3
"""
0-pascal's triangle
"""


def pascal_triangle(num):
    """
    returns a list of lists of
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

    for n in range(1, num+1):
        c = 1
        e = []
        for r in range(1, n+1):
            e.append(c)
            c = c*(n-r)//r
        a.append(e)
    return a
