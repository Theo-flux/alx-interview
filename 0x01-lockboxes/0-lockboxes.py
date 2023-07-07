#!/usr/bin/env python3
"""
python file for lockboxes function
"""
from typing import List, Union


def canUnlockAll(boxes: List[List[Union[int, None]]]) -> bool:
    """
    method to determine if all boxes can be opened

    Args:
        boxes (List[List[Union[int, None]]]): list if list of box param

    Returns:
        bool: return type
    """
    unlocked_boxes = [
        True if i == 0
        else False
        for i in range(len(boxes))
    ]

    # print("--before--")
    # print(unlocked_boxes)

    for i in range(len(boxes) - 1):
        if (len(boxes[i]) == 0):
            continue
        else:
            for j in range(len(boxes[i])):
                if (boxes[i][j] <= len(boxes) - 1):
                    unlocked_boxes[boxes[i][j]] = True

    # print("--after--")
    # print(unlocked_boxes, end='\n\n')

    return all(unlocked_boxes)
