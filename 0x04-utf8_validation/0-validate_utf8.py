#!/usr/bin/python3
"""
module for validating a 1-byte UTF-8
unicode code point
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """

    Args:
        data (List[int]): _description_

    Returns:
        bool: _description_
    """

    flag = True

    for i in range(len(data)):
        if (data[i] > 127):
            flag = False
            break

    return flag
