#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_tmp = []
    for x in matrix:
        matrix_tmp.append(list(map(lambda x: x**2, x)))
    return(matrix_tmp)
