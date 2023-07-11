#!/usr/bin/env python3
"""
min_operations file
"""


def minOperations(n) -> int:
    file_content = 'H'
    min_op = 0

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
