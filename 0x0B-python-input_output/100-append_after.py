#!/usr/bin/python3
""".................................."""


def append_after(filename="", search_string="", new_string=""):
    """ ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    """

    res_l = []
    with open(filename, 'r', encoding="utf-8") as f:
        for l in f:
            res_l += [l]
            if l.find(search_string) != -1:
                res_l += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_l))
