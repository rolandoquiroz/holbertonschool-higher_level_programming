#!/usr/bin/python3
"""
This module contains a function that returns
the list of available attributes and methods
of an object
"""


def lookup(obj):
    """list attributes and methods of object"""
    return (dir(obj))
