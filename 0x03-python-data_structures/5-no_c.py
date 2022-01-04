#!/usr/bin/env python3
def no_c(my_string):
    if my_string is None:
        return
    str_new = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            str_new += i
    return (str_new)
