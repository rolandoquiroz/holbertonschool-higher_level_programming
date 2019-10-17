#!/usr/bin/python3
"""
This module contains a function that
writes a string to a text file (UTF8)
and returns the number of characters written.

"""


def write_file(filename="", text=""):
    """
    write_file- Writes a string to a text file (UTF8).

    Args:
        filename(str): filename
        text(str): text

    Returns:
        The number of characters written.

    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
