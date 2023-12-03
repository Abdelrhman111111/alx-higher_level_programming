#!/usr/bin/python3
"""
......................
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]

    r = requests.get(u)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
