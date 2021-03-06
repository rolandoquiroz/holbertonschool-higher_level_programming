#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    """ this won't be run when imported """
    from sys import argv
    import MySQLdb

    """ Making a Connection """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    """
    Getting a Cursor
    A cursor object will let you execute all the queries you need
    """
    cursor = db.cursor()

    """
    Executing Queries
    Use all the SQL you like
    """
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    """
    Obtaining Query Results
    """
    states = cursor.fetchall()

    for state in states:
        print(state)
    """
    Clean Up
    Close all cursors and databases
    """
    cursor.close()
    db.close()
