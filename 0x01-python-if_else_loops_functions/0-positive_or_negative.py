#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    message = "{} is positive".format(number)
elif number == 0:
    message = "{} is zero".format(number)
else:
    message = "{} is negative".format(number)
    print(message)
