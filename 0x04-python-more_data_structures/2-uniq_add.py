#!/usr/bin/python3


def uniq_add(my_list=[]):
    e = []
    s = 0
    for x in my_list:
        if x not in e:
            s += x
            e.append(x)
    return s
