#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query to retrieve all states from the states table
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()

    # Close all database connections
    db.close()
