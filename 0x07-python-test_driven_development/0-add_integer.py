#!/usr/bin/python3
"""Modulus for addition
ss
ss
ss
"""


def add_integer(a, b=98):
    """Function that adds two integers and
         which checks if it is integer or float
         """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a+b)
