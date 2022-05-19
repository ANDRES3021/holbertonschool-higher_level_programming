#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ Returns a peak number from a unsorted list"""
    if len(list_of_integers) < 1:
        return None

    conjunto = set(list_of_integers)
    maximo = max(conjunto)
    return maximo
