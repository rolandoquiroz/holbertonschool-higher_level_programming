#!/usr/bin/python3
"""
This module contains a function that returns
the number of lines of a text file.

"""


def number_of_lines(filename=""):
    """
    number_of_lines- Counts the number of lines of a text file.

    Args:
        filename(str): filename

    Returns:
        The number of lines of a text file.

    """
    number_of_lines = 0
    nl = 0
    with open(filename, mode="r", encoding="utf-8") as a_file:
        nl = len(list(a_file))
        for a_line in a_file:
            number_of_lines += 1
    return (nl)
