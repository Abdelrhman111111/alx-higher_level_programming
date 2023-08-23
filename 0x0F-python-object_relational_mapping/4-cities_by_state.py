#!/usr/bin/python3
"""
.............................
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    ...............................
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        row = cur.fetchall()

    if row is not None:
        for r in row:
            print(r)
