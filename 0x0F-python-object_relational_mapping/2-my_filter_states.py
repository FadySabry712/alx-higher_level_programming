#!/usr/bin/python3
""" Filter states by user given input """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    myC = db.cursor()

    myC.execute(cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(sys.argv[4])))
    rows = myC.fetchall()
    for row in rows:
        print(row)

    myC.close()
    db.close()
