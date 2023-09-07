#!/usr/bin/python3
"""prime game mdoule"""


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return True


def get_multiples(n, arr):
    multiples = []
    for i in arr:
        if (n % i) == 0 and i != 1:
            multiples.append(i)
    return multiples


def isWinner(x, nums) -> str:
    turn = 1
    maria_score = 0
    ben_score = 0

    for round in range(x):
        array = list(range(1, nums[round]+1))
        pick = 0
        m_wins = 0
        b_wins = 0

        if len(array) == 1:
            if is_prime(array[0]):
                if turn % 2 != 0:
                    m_wins = m_wins + 1
                else:
                    b_wins = b_wins + 1
        else:
            temp = array
            for i in temp:
                if is_prime(i):
                    pick = i
                    if turn % 2 != 0:
                        m_wins = m_wins + 1
                    else:
                        b_wins = b_wins + 1
                for i in get_multiples(pick, temp):
                    temp.remove(i)
                turn = turn + 1

        if (m_wins > b_wins):
            maria_score = maria_score + 1
        elif (b_wins > m_wins):
            ben_score = ben_score + 1

    if (maria_score > ben_score):
        return 'Maria'
    if (ben_score > maria_score):
        return 'Ben'
    return 'Ben'
