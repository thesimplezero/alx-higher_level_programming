#!/usr/bin/python3

"""
Module for SQLAlchemy ORM setup, data insertion, and database connection.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

def main(database_username, database_password, database_name):
    """
    Main function to insert data into the database.
    
    Args:
        database_username (str): The database username.
        database_password (str): The database password.
        database_name (str): The database name.
    """
    engine = create_engine(
        f'mysql+mysqldb://{database_username}:{database_password}@localhost/{database_name}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco", state=state)

    session.add(state)
    session.add(city)

    session.commit()
    session.close()

if __name__ == "__main__":
    main(argv[1], argv[2], argv[3])
