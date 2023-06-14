#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #.

"""


def print_square(size):
    """
    print_square - Function that prints a square with the character #.

    Args:
        size: An integer with the size of the square.

    Returns:
        Nothing
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
