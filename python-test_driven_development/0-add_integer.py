#!/usr/bin/python3
"""
This module adds two integers.

"""


def add_integer(a, b=98):
    """
    add_integer- Function that adds two integers.

    Args:
        a: First number to be added.
        b: Second number to be added.

    Returns:
        The sum of a and b.
    """
    if ((type(a) != int) and (type(a) != float)):
        raise TypeError("a must be an integer")

    if ((type(b) != int) and (type(b) != float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
