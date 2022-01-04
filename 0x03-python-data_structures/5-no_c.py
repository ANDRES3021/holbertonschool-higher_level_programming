#!/usr/bin/env python3
def no_c(my_string):
    str_2 = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            str_2 += i
    return (str_2)
