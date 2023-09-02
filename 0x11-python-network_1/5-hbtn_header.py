#!/usr/bin/python3
""".......................
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]

    req = requests.get(u)
    print(req.headers.get("X-Request-Id"))
