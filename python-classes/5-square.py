#!/usr/bin/python3
"""
This is a module-level docstring.

This module provides an class for representing a square.

Classes
-------
Square: Defines a square.

Methods
-------
area: Calculate the area of the square.
my_print: Print the square.

Properties
----------
size: Retrieve or set the size of the square.
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

        Notes
        -----
        If size is not provided, the default value is 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns
        -------
        int
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters
        ----------
        value : int
            The new size value.

        Raises
        ------
        TypeError
            If value is not an integer.
        ValueError
            If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character #.

        If size is equal to 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
