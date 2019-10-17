#!/usr/bin/python3
"""
This file defines a function
that creates a pascals triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers
        representing the Pascal triangle of size n
    Args:
        n(int): size of Pascal triangle
    Returns:
        list of lists of integers representing Pascal triangle
    """
    res = []
    if n > 0:
        res.append([1])
        for r in range(1, n):
            pr = res[-1]
            res.append([1] + [pr[i - 1] + pr[i] for i in range(1, r)] + [1])
    return (res)
