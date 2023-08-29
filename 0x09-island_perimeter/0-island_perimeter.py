#!/usr/bin/python3
"""
island perimeter module
"""


def check_4_corners(i: int, j: int, grid) -> int:
    """
    checks the four corners of a cell

    Args:
        i (int): _description_
        j (int): _description_
        grid (List[List]): _description_

    Returns:
        int: _description_
    """
    up = 0
    down = 0
    left = 0
    right = 0

    # vertical check
    if len(grid) > 1:
        if i == 0:
            # if i is 1 don't update up only down
            down = grid[i + 1][j]
        elif i == len(grid) - 1:
            # if i is last don't update down only up
            up = grid[i - 1][j]
        else:
            up = grid[i - 1][j]
            down = grid[i + 1][j]

    if len(grid[i]) > 1:
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


def island_perimeter(grid) -> int:
    """
    maps out the perimeter of an island

    Args:
        grid (List[List]): _description_

    Returns:
        int: _description_
    """
    perimeter = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            cell = grid[i][j]

            if cell == 1:
                perimeter = perimeter + 4
                checker = check_4_corners(i, j, grid)
                perimeter = perimeter - checker

    return perimeter
