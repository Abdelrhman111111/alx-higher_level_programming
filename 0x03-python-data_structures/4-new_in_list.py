#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = len(my_list)
    lcpy = my_list.copy()
    if idx < 0:
        return lcpy
    elif idx > x - 1:
        return lcpy
    else:
        lcpy[idx] = element
        return lcpy
