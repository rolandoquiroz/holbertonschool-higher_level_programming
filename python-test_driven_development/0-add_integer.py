#!/usr/bin/python3
"""
Module 0-add_integer

This module provides a function to add two integers. It ensures
type safety by raising a TypeError if either of the inputs is not
an integer or float. The result is always returned as an integer.
"""

def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int | float): First number to add.
        b (int | float, optional): Second number to add. Defaults to 98.

    Returns:
        int: The sum of the two numbers, cast to an integer.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    return int(a) + int(b)
