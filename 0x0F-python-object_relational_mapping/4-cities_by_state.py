#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    """ This won't be run when imported """
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
    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id"
    )
    """
    Obtaining Query Results
    """
    cities = cursor.fetchall()

    for city in cities:
        print(city)
    """
    Clean Up
    Close all cursors and databases
    """
    cursor.close()
    db.close()
