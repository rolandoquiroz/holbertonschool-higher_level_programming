#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return (None)
    return (sorted(my_list)[-1])
