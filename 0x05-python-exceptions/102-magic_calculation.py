#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception('Too far')
            r += a ** b / n
        except Exception:
            r = b + a
            break
    return r
