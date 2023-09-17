#!/usr/bin/python3

"""
Script to query and display states from MySQL database
"""

import MySQLdb
from sys import argv

def connect_to_mysql(username, password, database):
    """
    Connect to a MySQL database using MySQLdb.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database.

    Returns:
        MySQLdb.connections.Connection: A MySQL database connection.
    """
    try:
        my_db = MySQLdb.connect(
            host='localhost', port=3306, user=username, passwd=password, db=database
        )
        return my_db
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def main():
    """
    Main function to connect to MySQL and fetch matching states.
    """
    if __name__ == "__main__":
        # Command-line arguments
        username = argv[1]
        password = argv[2]
        database = argv[3]
        search_state = argv[4]

        # Connect to MySQL database
        my_db = connect_to_mysql(username, password, database)
        if not my_db:
            return

        try:
            # Create cursor obj to interact with database
            my_cursor = my_db.cursor()

            # Execute a SELECT query to fetch data
            query = f"SELECT * FROM states WHERE name LIKE BINARY '{search_state}' ORDER BY states.id ASC"
            my_cursor.execute(query)

            # Fetch all the data returned by the query
            my_data = my_cursor.fetchall()

            # Iterate through the fetched data and print each row
            for row in my_data:
                print(row)

        except Exception as e:
            print(f"Error executing query: {e}")

        finally:
            # Close all cursors
            my_cursor.close()

            # Close all databases
            my_db.close()

if __name__ == "__main__":
    main()
