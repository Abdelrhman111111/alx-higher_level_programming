#!/usr/bin/python3
"""
............................
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    .................................
    """

    d = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], d=argv[3])

    with d.cursor() as c:
        c.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = c.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
