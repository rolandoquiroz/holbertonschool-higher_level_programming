#!/usr/bin/python3
"""
This module has a function
that adds new attribute to an obj

"""


def add_attribute(obj, key, value):
    """ Function add_attribute """
    if not isinstance(key, (int, str, tuple, float, bool, complex, range)):
        raise TypeError("can't add new attribute")
    elif not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        obj.__dict__[key] = value
