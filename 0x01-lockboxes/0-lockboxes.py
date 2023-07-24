#!/usr/bin/python3
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
    unlocked = set()

    for id, box in enumerate(boxes):
        if len(box) == 0 or id == 0:
            unlocked.add(id)
        for key in box:
            if key < len(boxes) and key != id:
                unlocked.add(key)
        if len(unlocked) == len(boxes):
            return True
    return False
