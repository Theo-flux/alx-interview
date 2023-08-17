#!/usr/bin/python3
"""
Rotate 2D Matrix module
"""
from typing import List


def rotate_2d_matrix(matrix: List[List]) -> None:
    """
    rotate a 2 dimensional matrix

    Args:
        matrix (List[List]): _description_
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = matrix[j][i]

    for i in range(n//2):
        for j in range(n):
            matrix[j][i], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[j][i]
