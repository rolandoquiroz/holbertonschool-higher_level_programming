#!/usr/bin/python3
import numpy
"""
Module to multiply matrix

"""


def lazy_matrix_mul(m_a, m_b):
    """
    Method to multiplies two matrix

    """
    try:
        ans = numpy.matmul(m_a, m_b)
    except:
        raise
    return ans

