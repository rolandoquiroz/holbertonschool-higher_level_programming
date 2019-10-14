#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.

"""


def text_indentation(text):
    """
    matrix_divided- Function that divides all elemets of a matrix.

    Args:
        matrix: List of lists to be divided.
        div: divisor.

    Returns:
        A matrix with te result of division.
    """

    if (type(text) != str):
        raise TypeError("text must be a string")
    new = "".join(ch if ch not in '?.:' else ch + "\n\n" for ch in text)
    l_l = new.split('\n')
    new = ""
    for line in l_l:
        new += '\n' + (line.strip())
    new = new[1:]
    print(new, end="")
