#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list_copied = my_list[:]
        my_list_copied[idx] = element
        return (my_list_copied)
    return my_list
