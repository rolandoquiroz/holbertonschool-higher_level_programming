#!/usr/bin/python3
"""
This module contains a function that returns True
if the object is an instance of, or if the object
is an instance of a class that inherited from, the
specified class

"""


def is_kind_of_class(obj, a_class):
    """function to determine if a an object is of a class or
    subclass
    """
    return (isinstance(obj, a_class))
