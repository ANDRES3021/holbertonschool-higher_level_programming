#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
     modul = number % 10  
    else:
     modul = number *-1 % 10
    print('{:d}'.format(modul), end="")
    return(modul)
