#!/usr/bin/python3
"""
Module that connects a Python script to a MySQL database.
"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State table ORM class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", back_populates="state")

class City(Base):
    """
    City table ORM class.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")

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
        search_state = argv[4]

        # Connect to MySQL database
        my_db = connect_to_mysql(username, password, database)
        if not my_db:
            return

        # Create SQLAlchemy engine and session
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Query and print cities and their corresponding states using SQLAlchemy
            cities = session.query(City).join(State).filter(State.name == search_state).order_by(City.id).all()
            for city in cities:
                print(city.name)

        except Exception as e:
            print(f"Error executing query: {e}")

        finally:
            # Close the SQLAlchemy session
            session.close()

        # Close the MySQLdb connection
        my_db.close()

if __name__ == "__main__":
    main()
