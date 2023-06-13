#!/usr/bin/python3
"""
This is a module-level docstring.

This module provides an class for representing a square.

Classes:
    - Square: Defines a square.
"""


class Square:
    """
    Defines a square.

    This class can be used to create square objects with a specific size.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Parameters
        ----------
        size : The size of each side of the square.
        """
        self.__size = size
