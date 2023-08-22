#!/usr/bin/python3
"""
......................................
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    .........................
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = c.fetchall()

    for r in rows:
        print(r)
