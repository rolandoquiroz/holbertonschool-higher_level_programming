#!/usr/bin/python3
"""
This module has a class MyList that inherits from
list. Has a public instance method print_sorted that
prints the list in ascending order

"""


class MyList(list):
    """MyList class subclass of list
    Attributes:
    print_sorted: prints the list in a sorted fashion
    """

    def print_sorted(self):
        """print_sorted method prints list sorted"""
        print(sorted(self))
