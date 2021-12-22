#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0 and (number % 10) < 6:
    str = 'and is less than 6 and not 0'
    print("Last digit of {:d} is {:d} {:s}".format(number, number % 10, str))
elif (number % 10) > 6:
    str1 = 'and is greater than 5'
    str1a = 'Last digit of'
    print(("{} {} is {} {}".format(str1a, number, number % 10, str1)))
elif number % 10 == 0:
    str2 = 'and is  0'
    str1a = 'Last digit of'
    print(("{} {} is {} {}".format(str1a, number, number % 10, str2)))
else:
    str3 = 'and is less than 6 and not 0'
    str1b = 'Last digit of'
    print(("{} {} is {} {}".format(str1b, number, number % -10, str3)))
