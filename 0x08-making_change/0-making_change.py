#!/usr/bin/env python3
"""
making change module
"""
from typing import List


def makeChange(coins: List, total: int) -> int:
    """
    make change

    Args:
        coins (List): _description_
        total (int): _description_

    Returns:
        int: _description_
    """
    if total <= 0:
        return 0

    change = 0
    coins = sorted(coins, reverse=True)

    while len(coins) != 0:
        max_coin = coins[0]

        if max_coin <= total:
            total = total - max_coin
            change = change + 1

            if max_coin > total:
                coins.pop(0)
        else:
            coins.pop(0)

    if total == 0:
        return change
    else:
        return -1
