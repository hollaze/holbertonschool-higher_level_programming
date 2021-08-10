#!/usr/bin/python3
""" Filter states by user input"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{}'".format(argv[4]))

    print(cursor.fetchone())

    cursor.close()
    db.close()
