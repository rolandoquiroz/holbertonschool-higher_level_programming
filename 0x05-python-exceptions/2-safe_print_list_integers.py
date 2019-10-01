#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end='')
            cnt += 1
    except (ValueError, TypeError, IndexError):
        pass
    print()
    return (cnt)
