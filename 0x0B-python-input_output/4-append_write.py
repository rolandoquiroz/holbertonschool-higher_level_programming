#!/usr/bin/python3
"""
This module contains a function that
appends a string at the end of a text
file (UTF8) and returns the number of
characters added.

"""


def append_write(filename="", text=""):
    """
    append_write- Appends a string at the end of a text file (UTF8).

    Args:
        filename(str): filename
        text(str): text

    Returns:
        The number of characters added.

    """
    with open(filename, 'a+', encoding='utf-8') as f:
        return f.write(text)
