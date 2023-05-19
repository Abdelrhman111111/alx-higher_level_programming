#!/usr/bin/python3


def uniq_add(my_list=[]):
    n = []
    s = 0
    for x in my_list:
        if n not in n:
            s += x
            n.append(x)
    return s
