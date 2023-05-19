#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    n = {}
    for x, y in a_dictionary.items():
        n.update({x: (y * 2)})
    return n
