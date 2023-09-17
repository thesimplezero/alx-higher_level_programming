#!/usr/bin/python3
"""
Module that connects a Python script to a MySQL database using MySQLdb and SQLAlchemy
"""

import MySQLdb
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

def connect_to_mysql(username, password, database):
    """
    Connect to MySQL database using MySQLdb and SQLAlchemy.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database.

    Returns:
        MySQLdb.connections.Connection: A MySQL database connection.
    """
    try:
        my_db = MySQLdb.connect(
            host='localhost', user=username, password=password, db=database, port=3306
        )
        return my_db
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def main():
    """
    Main function to connect to MySQL and fetch data from the 'states' table.
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

        # Create SQLAlchemy engine and session
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Execute a SELECT query using SQLAlchemy
            query = text("SELECT * FROM states ORDER BY states.id ASC;")
            result = session.execute(query)

            # Iterate through the fetched data and print each row
            for row in result:
                print(row)

        except Exception as e:
            print(f"Error executing query: {e}")

        finally:
            # Close the SQLAlchemy session
            session.close()

        # Close the MySQLdb connection
        my_db.close()

if __name__ == "__main__":
    from sys import argv
    main()
