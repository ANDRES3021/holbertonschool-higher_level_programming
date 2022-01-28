#!/usr/bin/python3
"""Module to divide a matrix
Divide each element of a matrix
of numbers by a number
"""


from operator import length_hint


def matrix_divided(matrix, div):
    """
    Function that divides all elements of an array
    """
    error_message = "matrix must be a matrix(list of lists) of integers/floats"
    if not matrix:
        raise TypeError(error_message)
    if not isinstance(matrix, list):
        raise TypeError(error_message)
    for lists_iterator in matrix:
        length_lists = len(lists_iterator)
        if not isinstance(lists_iterator, list):
            raise TypeError(error_message)
        for items_lists in lists_iterator:
            if not isinstance(items_lists, (int, float)):
                raise TypeError(error_message)
    for lists_iterator in matrix:
        if len(lists_iterator) == 0:
            raise TypeError(error_message)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if not all((length_lists) == len(matrix[0])for length_lists in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(items_lists/div, 2) for items_lists in lists_iterator] for lists_iterator in matrix]
