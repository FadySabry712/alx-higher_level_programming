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
    myCur = db.cursor()

    query = """
    SELECT states.id, name FROM states WHERE name='{:s}'
    COLLATE latin1_general_cs
    ORDER BY states.id ASC;
    """.format(state_name)

    myCur.execute(query)
    rows = myCur.fetchall()
    for row in rows:
        print(row)

    myCur.close()
    db.close()
