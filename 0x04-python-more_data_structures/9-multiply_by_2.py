#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary_tmp = a_dictionary.copy()
    for i in a_dictionary_tmp.keys():
        a_dictionary_tmp[i] *= 2
    return(a_dictionary_tmp)
