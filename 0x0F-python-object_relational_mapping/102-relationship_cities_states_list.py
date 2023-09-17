#!/usr/bin/python3

"""
Lists all City objects from the database hbtn_0e_101_usa
and connects to the database using SQLAlchemy module.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

def main(database_username, database_password, database_name):
    """
    Main function to list all City objects.
    
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

    for city in session.query(City).order_by(City.id):
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()

if __name__ == "__main__":
    main(argv[1], argv[2], argv[3])
