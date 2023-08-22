#!/usr/bin/python3
"""
................................
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    """
    d = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], d=argv[3])

    cur = d.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
