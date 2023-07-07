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
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
