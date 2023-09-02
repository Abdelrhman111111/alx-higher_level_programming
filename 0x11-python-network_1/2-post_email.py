#!/usr/bin/python3
"""
..........................
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    u = sys.argv[1]
    v = {"email": sys.argv[2]}
    d = urllib.parse.urlencode(v).encode("ascii")

    request = urllib.request.Request(u, d)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
