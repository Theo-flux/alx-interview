#!/usr/bin/env python3
"""
python file for lockboxes function
"""
from typing import List, Union


def canUnlockAll(boxes: List[Union[List[int], List]]) -> bool:
    """
    method to determine if all boxes can be opened

    Args:
        boxes (List[Union[List[int], List[]]]): list if list of box param

    Returns:
        bool: return type
    """
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
