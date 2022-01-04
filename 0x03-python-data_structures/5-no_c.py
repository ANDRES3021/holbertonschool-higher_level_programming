#!/usr/bin/env python3
def no_c(my_string):
    str_new = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            str_new += i
    return (str_new)
