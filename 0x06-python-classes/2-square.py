#!/usr/bin/python3
class Square:
    """Defines a class square
    """

    def __init__(self, size=0):
        """Square object attributes initialization.

        Args:
            size: Square size must be integer and equals or greater than zero.

        Returns:
            None.

        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
