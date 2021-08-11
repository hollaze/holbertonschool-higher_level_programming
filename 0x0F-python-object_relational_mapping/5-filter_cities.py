#!/usr/bin/python3
"""All cities by state"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT cities.name "
                   "FROM cities "
                   "INNER JOIN states "
                   "ON cities.state_id = states.id "
                   "WHERE states.name=%s "
                   "ORDER BY cities.id ASC", [argv[4]])

    rows = cursor.fetchall()
    try:
        for row in range(len(rows)):
            print(rows[row][0], ', ' if row < len(rows) - 1 else ' ', end='')
        print()
    except:
        print()

    cursor.close()
    db.close()
