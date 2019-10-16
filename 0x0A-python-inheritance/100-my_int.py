#!/usr/bin/python3
"""
This modules contains a class
that inherits from int

"""


class MyInt(int):
    """Class MyInt"""
    def __eq__(self, other):
        """eq magic method"""
        return False

    def __ne__(self, other):
        """ne magic method"""
        return True
