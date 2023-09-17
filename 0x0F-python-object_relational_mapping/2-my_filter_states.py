#!/usr/bin/python3

"""
Module to list all states from the hbtn_0e_0_usa database.
"""

import sys
import MySQLdb
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State table ORM class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

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
            user=username, passwd=password, db=database
        )
        return my_db
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def main():
    """
    Main function to list all states from MySQL database.
    """
    if __name__ == "__main__":
        # Command-line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        search_state = sys.argv[4]

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
            query = select([State]).where(State.name == search_state)
            result = session.execute(query)

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
    main()
