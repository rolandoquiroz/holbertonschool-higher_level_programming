#!/usr/bin/python3
import json
"""
This module contains a function that
returns the JSON representation of an
object (string).

"""


def to_json_string(my_obj):
    """
    to_json_string- Writes a string to a text file (UTF8).

    Args:
        my_obj(str): stream object

    Returns:
        The JSON representation of an object (string).

    """
    return (json.dumps(my_obj))
