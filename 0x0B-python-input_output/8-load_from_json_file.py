#!/usr/bin/python3
import json
"""
This module contains a function that
creates an Object from a “JSON file”.

"""


def load_from_json_file(filename):
    """
    load_from_json_file- Creates an Object from a “JSON file”.

    Args:
        filename(str): filename

    Returns:
        Nothing.

    """
    with open(filename) as f:
        return (json.loads(f.read()))
