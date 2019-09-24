#!/usr/bin/python3
def no_c(my_string):
    return "".join(filter(lambda i: i not in "cC", my_string))
