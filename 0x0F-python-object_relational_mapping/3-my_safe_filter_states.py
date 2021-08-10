#!/usr/bin/python3
"""Safe from SQLInjection"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s", [argv[4]])

    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)

    cursor.close()
    db.close()
