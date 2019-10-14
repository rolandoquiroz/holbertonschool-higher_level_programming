#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    matrix_divided- Function that divides all elemets of a matrix.

    Args:
        matrix: List of lists to be divided.
        div: divisor.

    Returns:
        A matrix with te result of division.
    """
    err = 'matrix must be a matrix (list of lists) of integers/floats'

    if (type(matrix) != list):
        raise TypeError(err)
    for r in matrix:
        if (type(r) != list):
            raise TypeError(err)

    if (div == 0):
        raise ZeroDivisionError('division by zero')
    if ((type(div) != int) and (type(div) != float)):
        raise TypeError('div must be a number')

    for r in matrix:
        for e in r:
            if ((type(e) != int) and (type(e) != float)):
                raise TypeError(err)

    length_of_rs = []
    for r in matrix:
        length_of_rs.append(len(r))
    length_of_rs = set(length_of_rs)
    if len(length_of_rs) > 1:
        raise TypeError('Each r of the matrix must have the same size')

    new_matrix = []
    for r in matrix:
        new_matrix.append([round((x/div), 2) for x in r])
    return new_matrix
