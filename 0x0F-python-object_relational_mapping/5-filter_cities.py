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

    list = []

    for row in rows:
        for column in row:
            list.append(column)
    print(", ".join(list))

    cursor.close()
    db.close()
