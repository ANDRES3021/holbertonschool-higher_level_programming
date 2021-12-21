#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0 and (number % 10) < 6:
    print(("Last digit of {:d} is".format(number)),"{:d} and is less than 6 and not 0".format((number % 10)))
elif (number % 10) > 6:
    print(("Last digit of {:d} is".format(number)),"{:d} and is greater than 5".format((number % 10)))
elif number % 10 == 0:
     print(("Last digit of {:d} is".format(number)),"{:d} and is  0".format((number % 10)))
else:
    print(("Last digit of {:d} is".format(number)),"{:d} and is less than 6 and not 0".format((number % -10)))
    