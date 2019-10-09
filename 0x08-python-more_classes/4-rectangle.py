#!/usr/bin/python3
"""
This module defines a class Rectangle

"""


class Rectangle:

    """
    Rectangle Class

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle

    """

    def __init__(self, width=0, height=0):
        """
        Rectangle object attributes initialization method.

        Args:
            width (int): width of Rectangle.
            heigth (int): heigth of Rectangle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter width method.

        Returns:
            width: Private width attribute value.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width method.

        Args:
        value: width value to be setted.

        Raises:
            TypeError: when width is not a integer.
            ValueError: when width is less than zero.

        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter height method.

        Returns:
            height: Private height attribute value.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height method.

        Args:
           value: height value to be setted.

        Raises:
            TypeError: when height is not a integer.
            ValueError: when height is less than zero.

        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Rectangle area calculation method.

        Returns:
            Area of the Rectangle

        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Rectangle perimeter calculation method.

        Returns:
            Perimeter of the Rectangle

        """

        if ((self.__width == 0) or (self.__height == 0)):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Rectangle print method.

        Returns:
            If width or height is equal to 0, return an empty string.
            Otherwise should print the rectangle with the character #.

        """
        other = ""
        if ((self.__width == 0) or (self.__height == 0)):
            return other
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                other += "#"
            if (i != self.__height - 1):
                other += "\n"
        return other

    def __repr__(self):
        """
        Rectangle string representation method.

        Returns:
            A string representation of the rectangle to be able to
            recreate a new instance by using eval().

        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))
