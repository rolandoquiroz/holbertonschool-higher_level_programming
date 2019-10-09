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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Rectangle object attributes initialization method.
        Also increases by one the counter of Rectangle objects.

        Args:
            width (int): width of Rectangle.
            heigth (int): heigth of Rectangle.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                other += str(self.print_symbol)
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

    def __del__(self):
        """
        Rectangle delete method.

        Returns:
            Print the message Bye rectangle... (... being 3 dots not ellipsis)
            when an instance of Rectangle is deleted.
              Also decreases by one the counter of Rectangle objects.

        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area.

        Args:
            rect_1: Instance of class Rectangle.
            rect_2: Instance of class Rectangle.

        Returns:
            The biggest rectangle based on the area.

        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_2.area() > rect_1.area():
            return (rect_2)
        return (rect_1)
