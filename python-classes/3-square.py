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

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Parameters
        ----------
        size : int, optional
            The size of each side of the square.

        Attributes
        ----------
        size : int
            The size of each side of the square. Default is 0.

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.

        Notes
        -----
        If size is not provided, the default value is 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2
