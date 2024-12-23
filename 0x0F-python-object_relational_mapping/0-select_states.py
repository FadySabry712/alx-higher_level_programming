#!/usr/bin/python3
''' a script that lists all states from the database hbtn_0e_0_usa '''

from sys import argv
import MYSQLdb

if __name__ == "main":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MYSQLdb.connect (
            host="localhost",
            user=username,
            passwd=password.
            db=db_name)
    myCursor = db.cursor()
    myCursor.excute("SELECT states.id, name FROM states ORDER BY states.id ASC;")
    rows = myCursor.fetchall()

    for row in rows:
        print(row)

    myCursor.close()
    db.close()
