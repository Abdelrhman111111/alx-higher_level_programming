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
    dp = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], dp=argv[3])

    c = dp.cursor()
    c.execute("SELECT * FROM states")
    r = c.fetchall()

    for row in r:
        print(row)
