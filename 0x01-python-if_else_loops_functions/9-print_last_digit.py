#!/usr/bin/python3
def print_last_digit(n):
    if n < 0:
        n = n * -1
    i = n % 10
    print("{}".format(i), end='')
    return i
