#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        ans = my_list[0]
        for i in my_list:
            if i > ans:
                ans = i
                return (ans)
    return (None)
