#!/usr/bin/python3
"""
..................................
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        c = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(c)))
        print("\t- content: {}".format(c))
        print("\t- utf8 content: {}".format(c.decode('utf-8')))
