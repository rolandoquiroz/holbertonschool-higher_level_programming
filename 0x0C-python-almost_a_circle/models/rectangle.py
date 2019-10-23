#!/usr/bin/python3
"""
This is a Rectangle class

"""
from models.base import Base
"""
Superclass Base

"""


class Rectangle(Base):
    """
    subclass Rectangle

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instance attributes initialization

        Args:
            width (int): width
            height (int): height
            x (int) = x
            y (int) = y
            id (int) = id

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        width getter method

        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width setter method

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter method

        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height setter method

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        x getter method

        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        x setter method

        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        y getter method

        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        y setter method

        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        area method returns the area value of
        the Rectangle instance.

        """
        return (self.__width * self.__height)

    def display(self):
        """
        display method prints in stdout the
        Rectangle instance with the character #

        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        string magic method returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>

        """
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        method that assigns an argument to each attribute

        """
        if ((args is not None) and (len(args)) > 0):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]

        elif ((kwargs is not None) and (len(kwargs)) > 0):
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "width":
                    self.__width = kwargs[key]
                if key == "height":
                    self.__height = kwargs[key]
                if key == "x":
                    self.__x = kwargs[key]
                if key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """
        dictionary representation of a Rectangle

        """
        r_dict = {"id": 0, "width": 0, "height": 0, "x": 0, "y": 0}
        for key in r_dict:
            if key == "id":
                r_dict[key] = self.id
            if key == "width":
                r_dict[key] = self.width
            if key == "height":
                r_dict[key] = self.height
            if key == "x":
                r_dict[key] = self.x
            if key == "y":
                r_dict[key] = self.y
        return (r_dict)
