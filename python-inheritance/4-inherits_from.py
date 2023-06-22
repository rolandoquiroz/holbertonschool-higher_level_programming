#!/usr/bin/python3
"""
This module contains a function that returns
True if the object is an instance of a class
that inherited (directly or indirectly) from
the specified class

"""


def inherits_from(obj, a_class):
    """function to determine if the type of obj is inherited"""

    if type(obj) != a_class:
        return isinstance(obj, a_class)
    return False
