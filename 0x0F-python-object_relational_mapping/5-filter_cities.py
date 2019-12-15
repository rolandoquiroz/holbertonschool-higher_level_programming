#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
        "SELECT cities.id, cities.name \
        FROM states JOIN cities ON cities.state_id = states.id \
        WHERE states.name = %(states.name)s \
        ORDER BY cities.id", {'states.name': argv[4]}
    )
    """
    Obtaining Query Results
    """
    cities = cursor.fetchall()

    for i, city in enumerate(cities):
        if i:
            print(', ', end='')
        print(city[1], end='')
    print()

    """
    Clean Up
    Close all cursors and databases
    """
    cursor.close()
    db.close()
