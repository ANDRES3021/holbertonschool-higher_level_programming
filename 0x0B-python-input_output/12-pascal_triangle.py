#!/usr/bin/python3
"""Module 14"""


def pascal_triangle(n):
    """Pascal triangle"""

    if n <= 0:
        return []
    list_1 = [[1]]
    tmp = []
    for i in range(n - 1):
        tmp = tmp.copy()
        tmp = []
        tmp.append(1)
        for j in range(i):
            tmp.append(list_1[i][j] + list_1[i][j + 1])
        tmp.append(1)
        list_1.append(tmp)
    return list_1
