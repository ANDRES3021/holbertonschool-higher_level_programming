#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return(x is list(map(lambda x: replace if search else x, my_list)))
