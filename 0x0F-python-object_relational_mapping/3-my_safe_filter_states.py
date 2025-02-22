#!/usr/bin/python3
"""takes in an argument and displays all values
in the states table """

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    myC = db.cursor()
    myC.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    rows = myC.fetchall()
    for row in rows:
        print(row)

    myC.close()
    db.close()
