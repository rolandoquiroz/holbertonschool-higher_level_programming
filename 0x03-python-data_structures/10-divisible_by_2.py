#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ans = []
    for i in my_list:
        if i % 2:
            ans.append(False)
        else:
            ans.append(True)
    return ans
