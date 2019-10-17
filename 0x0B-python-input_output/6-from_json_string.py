#!/usr/bin/python3
import json
"""
This module contains a function that
returns an object (Python data structure)
represented by a JSON string.

"""


def from_json_string(my_str):
    """
    from_json_string- Writes a string to a text file (UTF8).

    Args:
        my_str(str): stream object

    Returns:
        An object (Python data structure) represented by a JSON string.

    """
    return (json.loads(my_str))
