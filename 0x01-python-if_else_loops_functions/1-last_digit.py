#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    modul = number % 10
    number2 = number
else:
    modul = (((number * (- 1)) % 10) * -1)
    number2 = number
if modul == 0:
    print("Last digit of {} is {} and is 0".format(number, modul))
elif modul > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, modul))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number2, modul))
