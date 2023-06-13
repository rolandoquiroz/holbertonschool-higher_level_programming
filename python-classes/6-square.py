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
position: Retrieve or set the position of the square.
"""


class Square:
    """
    Defines a square.

    This class can be used to create square objects
    with a specific size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Parameters
        ----------
        size : int, optional
            The size of each side of the square.
        position : tuple of 2 positive integers, optional
            The position of the square.

        Attributes
        ----------
        size : int
            The size of each side of the square. Default is 0.
        position : tuple of 2 positive integers
            The position of the square. Default is (0, 0).

        Notes
        -----
        If size or position are not provided,
        the default values are 0 for size and (0, 0) for position.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Get the position of the square.

        Returns
        -------
        tuple
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Parameters
        ----------
        value : tuple
            The new position value.

        Raises
        ------
        TypeError
            If value is not a tuple or not of length 2
            or not containing positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or 
            not isinstance(value[0], int) or not isinstance(value[1], int) or 
            value[0] < 0 or value[1] < 0): 
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        The position is taken into account when printing the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
