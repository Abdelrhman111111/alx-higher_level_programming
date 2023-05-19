#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        l = list(a_dictionary.keys())
        s = 0
        d = ""
        for x in l:
            if a_dictionary[x] > s:
                s = a_dictionary[x]
                d = x
        return d
