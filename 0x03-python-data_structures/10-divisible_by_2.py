#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = []
    for x in my_list:
        if x % 2 == 0:
            n.append(True)
        else:
            n.append(False)
    return n
