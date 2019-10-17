#!/usr/bin/python3
"""
This module creates a student class
with public attributes and retrives
json dictionary representation

"""


class Student:
    """
    Class Student

    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize instance attributes

        Args:
            first_name(str): first name
            last_name(str): last name
            age(int): age

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation
        of a Student instance

        Args:
            attrs(list): a attributes list

        Returns:
            A dictionary representation of a Student instance

        """
        if (attrs is None):
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})

    def reload_from_json(self, json):
        """
        Updates all attributes of the Student instance

        Args:
            json(dict): a dictionary

        """
        self.__dict__.update(json)
