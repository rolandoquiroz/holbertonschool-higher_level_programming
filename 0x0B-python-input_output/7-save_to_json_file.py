#!/usr/bin/python3
import json
"""
This module contains a function that
writes an Object to a text file, using
a JSON representation.

"""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file- Writes an Object to a text file,
    using a JSON representation.

    Args:
        my_obj(str): stream object
        filename(str): filename

    Returns:
        Nothing.

    """
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
