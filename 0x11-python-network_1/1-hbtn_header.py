#!/usr/bin/python3
"""
.........................
"""
import sys
import urllib.request

if __name__ == "__main__":
    u = sys.argv[1]

    req = urllib.req.Request(u)
    with urllib.req.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
