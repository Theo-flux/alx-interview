#!/usr/bin/env python3
"""
min_operations file
"""


def minOperations(n) -> int:
    min_op = 0

    if n < 2:
        return min_op

    file_content = 'H'


    while len(file_content) < n:
        copyAll = file_content
        min_op += 1

        if len(copyAll + file_content) < n:
            file_content += copyAll
            min_op += 1
            file_content += copyAll
            min_op += 1
        else:
            break

    return min_op
