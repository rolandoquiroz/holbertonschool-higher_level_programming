#!/usr/bin/python3
class Square:
    """Defines a class square
    """
    def __init__(self, size=0):
        """Initialize the sise of the square

        Args:
            self: The object itself.
            size: The size of the square.

        Returns:
            None.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square

        Args:
            self: The object itself.

        Return: The size field of the object.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Square object attributes initialization.

        Args:
            self: The object itself.
            value: The value to be setted on size field.

        Returns:
            None.
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Method to calculate a square area object.

        Args:
            self: The object itself.

        Returns:
            The area of a square.
        """
        return (self.__size ** 2)
