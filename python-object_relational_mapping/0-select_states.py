#!/usr/bin/python3
"""
Python script that list all states from table states
from database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    """ This code won't be run when imported """

    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id;")

    states = cursor.fetchall()

    for _ in states:
        print(_)

    cursor.close()
    db.close()
