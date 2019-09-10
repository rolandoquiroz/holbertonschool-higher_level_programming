#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
my_str = ['Last digit of', 'is', 'and is 0', 'and is greater than 5',
     'and is less than 6 and not 0']
l_d = number % 10 if number >= 0 else (abs(number) % 10) * -1
print(my_str[0], number, my_str[1], l_d, my_str[2] if l_d == 0 else my_str[3] if l_d > 5 else my_str[4])
