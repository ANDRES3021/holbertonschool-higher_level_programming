#!/usr/bin/python3
def matrix_divided(matrix, div):
    error_message = 'matrix must be a matrix (list of lists) of integers/floats'
    if not matrix:
        raise TypeError(error_message)
    if not isinstance(matrix, list):
        raise TypeError(error_message) 
    for lists_iterator in matrix:
        if not isinstance (lists_iterator, list):
            raise TypeError(error_message)
        for items_lists in lists_iterator:
            if not isinstance(items_lists, int) and not isinstance(items_lists, float):
                raise TypeError(error_message)
    for lists_iterator in matrix:
        if len(lists_iterator) == 0:
            raise TypeError(error_message)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if not all(len(lists_iterator) == len(matrix[0]) for lists_iterator in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(items_lists / div, 2) for items_lists in lists_iterator] for lists_iterator in matrix ]
