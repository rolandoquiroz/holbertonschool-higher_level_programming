#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """
        Initializes validated private instace vars \
        __width and __height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
