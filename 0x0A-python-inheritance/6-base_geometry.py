#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required

"""


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """area method raises exception"""
        raise Exception("area() is not implemented")
