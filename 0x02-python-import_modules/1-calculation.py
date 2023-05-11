#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import a, s, d, m
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, a(a, b)))
    print("{} - {} = {}".format(a, b, s(a, b)))
    print("{} * {} = {}".format(a, b, m(a, b)))
    print("{} / {} = {}".format(a, b, d(a, b)))
