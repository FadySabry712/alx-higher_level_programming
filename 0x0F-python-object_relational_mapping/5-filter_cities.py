#!/usr/bin/python3
""" All cities by state name"""

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

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    myC.execute(query, (state_name,))

    rows = myC.fetchall()
    rows = [i[0] for i in rows]

    print(', '.join(rows))

    myC.close()
    db.close()
