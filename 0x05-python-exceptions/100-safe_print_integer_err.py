#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError) as to:
        stderr.write('Exception: {}\n'.format(to))
        return (False)
    return (True)
