#!/usr/bin/python3
"""
This module contains a function that
reads n lines of a text file (UTF8)
and prints it to stdout.

"""


def read_lines(filename="", nb_lines=0):
    """
    read_lines- Reads n lines of a text
    file (UTF8) and prints it to stdout:

    Args:
        filename(str): filename
        nb_lines(int): nb_lines

    Returns:
        The number of lines of a text file.

    """
    with open(filename, 'r', encoding='utf-8') as f:
        if ((nb_lines <= 0) or (nb_lines > len(list(filename)))):
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
