#!/usr/bin/python3
""" .........................."""


def pascal_triangle(n=4500):
    """........................"""
    p = [[0]*x for x in range(1, n+1)]
    c = 0
    for x in range(n):
        p[x][0] = 1
        p[x][-1] = 1
        for y in range(0, x//2):
            p[x][y+1] = p[x-1][y] + p[x-1][y+1]
            p[x][x-y-1] = p[x-1][y] + p[x-1][y+1]

    return p
