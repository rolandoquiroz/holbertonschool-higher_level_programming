#!/usr/bin/python3
""" Python script that list all states from table hbtn_0e_0_usa.states """

if __name__ == "__main__":
    """ This code won't be run when imported """

    from sys import argv
    import MySQLdb

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id;")

    states = cursor.fetchall()

    for _ in states:
        print(_)

    cursor.close()
    database.close()
