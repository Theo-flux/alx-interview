#!/usr/bin/env python3
"""island perimeter module"""
from typing import List


def check_4_corners(i: int, j: int, grid: List[List]) -> int:
    pass
    up = 0
    down = 0
    left = 0
    right = 0

    # vertical check
    if i == 0:
        # if i is 1 don't update up only down
        down = grid[i + 1][j]
    elif i == len(grid) - 1:
        # if i is last don't update down only up
        up = grid[i - 1][j]
    else:
        up = grid[i - 1][j]
        down = grid[i + 1][j]

    if j == 0:
        # if j is 1 don't update left only right
        right = grid[i][j + 1]
    elif j == len(grid[i]) - 1:
        # if j is last don't update right only left
        left = grid[i][j - 1]
    else:
        left = grid[i][j - 1]
        right = grid[i][j + 1]

    return up + down + left + right


def island_perimeter(grid: List[List]) -> int:
    perimeter = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            cell = grid[i][j]

            if cell == 1:
                perimeter = perimeter + 4
                checker = check_4_corners(i, j, grid)
                perimeter = perimeter - checker

    return perimeter
