#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_tmp = my_list[:]
    if 0 <= idx < len(my_list):
        list_tmp[idx] = element
        return(list_tmp)
    return(my_list)
