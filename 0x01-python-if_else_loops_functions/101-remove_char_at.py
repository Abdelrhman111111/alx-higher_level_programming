#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    c = 0
    str_c = ""
    for elem in str:
        if c == n:
            c += 1
            continue
        str_c += str[c]
        c += 1
    return str_c
