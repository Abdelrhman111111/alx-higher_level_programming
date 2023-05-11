#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import a, s, d, m
    x = 10
    y = 5
    print("{} + {} = {}".format(x, y, a(x, y)))
    print("{} - {} = {}".format(x, y, s(x, y)))
    print("{} * {} = {}".format(x, y, m(x, y)))
    print("{} / {} = {}".format(x, y, d(x, y)))
