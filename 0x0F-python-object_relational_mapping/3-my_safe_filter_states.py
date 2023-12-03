#!/usr/bin/python3
"""Script that takes in an argument and displays all values
in the `states` table of the database `hbtn_0e_0_usa` where
`name` matches the argument, safe from MySQL injection.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")

    # Create a cursor object
    cur = db.cursor()

    # Use format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()

    # Close all database connections
    db.close()
