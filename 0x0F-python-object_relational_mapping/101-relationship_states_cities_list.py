#!/usr/bin/python3

"""
Module for SQLAlchemy ORM setup and querying data from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

def main(database_username, database_password, database_name):
    """
    Main function to query data from the database and print it.
    
    Args:
        database_username (str): The database username.
        database_password (str): The database password.
        database_name (str): The database name.
    """
    engine = create_engine(
        f'mysql+mysqldb://{database_username}:{database_password}@localhost/{database_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()

if __name__ == "__main__":
    main(argv[1], argv[2], argv[3])
