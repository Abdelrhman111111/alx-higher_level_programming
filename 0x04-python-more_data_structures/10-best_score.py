#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        my = list(a_dictionary.keys())
        s = 0
        l = ""
        for x in my:
            if a_dictionary[i] > s:
                s = a_dictionary[x]
                l = x
        return l
