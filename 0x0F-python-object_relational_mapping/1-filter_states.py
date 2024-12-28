#!/usr/bin/python3
""" a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    myC = db.cursor()
    myC.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")

    rows = myC.fetchall()
    for row in rows:
        print(row)

    myC.close()
    db.close()
