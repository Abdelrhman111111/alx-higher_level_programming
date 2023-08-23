#!/usr/bin/python3
"""
............................
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    ...................................
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        row = cur.fetchall()

    if r is not None:
        print(", ".join([r[1] for r in row]))
