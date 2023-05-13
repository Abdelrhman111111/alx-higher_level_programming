#!/usr/bin/python3

def replace_in_list(my_list, idx,new_element):
    x = len(my_list)
    if idx < 0:
        return my_list
    elif idx > x - 1:
        return my_list
    else:
        my_list[idx] = new_element
        return my_list
