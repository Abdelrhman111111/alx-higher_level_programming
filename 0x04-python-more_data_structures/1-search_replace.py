#!/usr/bin/python3


def search_replace(my_list, search, replace):
    e = []
    for x in my_list:
        if x == search:
            e.append(replace)
        else:
            e.append(x)
    return e
