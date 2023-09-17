#!/usr/bin/python3

"""
Module that connects a Python script to a MySQL database
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
            host='localhost', port=3306, user=username, password=password, db=database
        )
        return my_db
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def fetch_states_starting_with_N(connection):
    """
    Fetch states whose names start with 'N' from the database.

    Args:
        connection (MySQLdb.connections.Connection): A MySQL database connection.

    Returns:
        list: A list of tuples representing the fetched data.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
        )
        return cursor.fetchall()
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")
        return []

def main():
    """
    Main function to connect to MySQL, fetch data, and print it.
    """
    if __name__ == "__main__":
        # Command-line arguments
        username = argv[1]
        password = argv[2]
        database = argv[3]

        # Connect to MySQL database
        my_db = connect_to_mysql(username, password, database)
        if not my_db:
            return

        # Fetch and print states starting with 'N'
        states = fetch_states_starting_with_N(my_db)
        for state in states:
            print(state)

        # Close the MySQLdb connection
        my_db.close()

if __name__ == "__main__":
    main()
