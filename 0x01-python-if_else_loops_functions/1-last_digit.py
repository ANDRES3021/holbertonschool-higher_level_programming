#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    mol = number % 10
    n2 = number
else:
    mol = (((number * (- 1)) % 10) * -1)
    n2 = number
if mol == 0:
    print("Last digit of {} is {} and is 0".format(number, mol))
elif mol > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, mol))
else:
    str = 'and is less than 6 and not 0'
    print("Last digit of {} is {} {}".format(n2, mol, str))
