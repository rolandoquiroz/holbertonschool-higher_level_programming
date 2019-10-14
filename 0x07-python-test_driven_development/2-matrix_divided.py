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
    if type(matrix) is not list:
        raise TypeError(err)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err)

    # make sure div is not 0
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    # make sure each element is an int or float
    for row in matrix:
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(err)

    # make sure all rows are the same size
    length_of_rows = []
    for row in matrix:
        length_of_rows.append(len(row))
    length_of_rows = set(length_of_rows)
    if len(length_of_rows) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    # finally, do the division and return the new matrix
    new_matrix = []
    for row in matrix:
        new_matrix.append([round((x/div), 2) for x in row])
    return new_matrix
