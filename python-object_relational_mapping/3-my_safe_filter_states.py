#!/usr/bin/env python3
"""
Python script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa database where name matches the argument.
But this time, it is safe from MySQL injections!
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

    cur = db.cursor()


    sql = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC;"
    args = (argv[4],)

    cur.execute(sql, args)

    states = cur.fetchall()

    for _ in states:
        print(_)

    cur.close()
    db.close()
