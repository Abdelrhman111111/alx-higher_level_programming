#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    k = list(a_dictionary.k())
    k.sort()
    for x in k:
        print("{}: {}".format(x, a_dictionary[x]))
