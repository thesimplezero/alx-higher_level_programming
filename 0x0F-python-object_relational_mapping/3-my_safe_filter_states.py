#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves states based on a provided name.
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

def fetch_states_by_name(connection, state_name):
    """
    Fetch states from the database by name.

    Args:
        connection (MySQLdb.connections.Connection): A MySQL database connection.
        state_name (str): The name of the state to search for.

    Returns:
        list: A list of tuples representing the fetched data.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id", (state_name, ))
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
        search_state = argv[4]

        # Connect to MySQL database
        my_db = connect_to_mysql(username, password, database)
        if not my_db:
            return

        # Fetch and print states by name
        states = fetch_states_by_name(my_db, search_state)
        for state in states:
            print(state)

        # Close the MySQLdb connection
        my_db.close()

if __name__ == "__main__":
    main()
