#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
my_str = ['Last digit of', 'is', 'and is 0', 'and is greater than 5',
     'and is less than 6 and not 0']
last_digit = number % 10 if number >= 0 else (abs(number) % 10) * -1
print(my_str[0], number, my_str[1], last_digit, my_str[2] if last_digit == 0 else my_str[3] if last_digit > 5 else my_str[4])
