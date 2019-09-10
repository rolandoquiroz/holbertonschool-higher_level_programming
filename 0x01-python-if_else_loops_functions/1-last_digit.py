#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % -10 if number < 0 else number % 10
desc = "0" if ld == 0 else "greater than 5" if ld > 5 else "less than 6 and not 0"
print("Last digit of {:d} is {:d} and is {}".format(number, ld, desc))
