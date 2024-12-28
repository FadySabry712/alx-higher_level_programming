#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument """

from sys import argv
import MYSQLdb

if __name__ = "__main__":
    username = argv[1]
    password = argv [2]
    db_name = argv[3]
    state_name = argv[3]

    db = MYSQLdb.connect(host="localhost",
            port=3306,
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
