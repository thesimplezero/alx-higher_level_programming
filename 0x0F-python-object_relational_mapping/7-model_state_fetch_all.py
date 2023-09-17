#!/usr/bin/python3

"""
Module that connects a Python script to a MySQL database and prints states using SQLAlchemy.
"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

        # Create SQLAlchemy engine and session
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Query and print states using SQLAlchemy
            for state in session.query(State).order_by(State.id):
                print("{}: {}".format(state.id, state.name))

        except Exception as e:
            print(f"Error executing query: {e}")

        finally:
            # Close the SQLAlchemy session
            session.close()

        # Close the MySQLdb connection
        my_db.close()

if __name__ == "__main__":
    main()
