#!/usr/bin/python3
"""
............................
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    .......................
    """
    d = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], d=argv[3])

    c = d.cursor()
    c.execute("SELECT * FROM states")
    r = c.fetchall()

    for row in r:
        print(row)
