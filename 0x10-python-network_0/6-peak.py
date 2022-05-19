#!/usr/bin/python3

from contextlib import nullcontext


def find_peak(list_of_integers):
    if len(list_of_integers) < 1:
        return None
    
    conjunto = set(list_of_integers)
    maximo = max(list_of_integers)
    return maximo