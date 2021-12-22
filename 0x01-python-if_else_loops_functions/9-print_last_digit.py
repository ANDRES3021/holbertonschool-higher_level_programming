#!/usr/bin/python3
def print_last_digit(number):
     modul = number % 10 if number > 0 else  number *-1 % 10
     print('{:d}'.format(modul), end="")
     return(modul)