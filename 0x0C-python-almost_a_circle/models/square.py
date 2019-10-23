#!/usr/bin/python3
"""
This is a Square class

"""
from models.rectangle import Rectangle
"""
Superclass Rectangle

"""


class Square(Rectangle):
    """
    subclass Rectangle

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instance attributes initialization

        Args:
            size (int):
            x (int) = x
            y (int) = y
            id (int) = id

        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str magic method

        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        size getter method

        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        size setter method

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        method that assigns an argument to each attribute

        """
        if ((args is not None) and (len(args) > 0)):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]

        elif ((kwargs is not None) and (len(kwargs)) > 0):
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "size":
                    self.size = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """
        dictionary representation of a Square

        """
        s_dict = {"id": 0, "size": 0, "x": 0, "y": 0}
        for key in s_dict:
            if key == "id":
                s_dict[key] = self.id
            if key == "size":
                s_dict[key] = self.size
            if key == "x":
                s_dict[key] = self.x
            if key == "y":
                s_dict[key] = self.y
        return (s_dict)
