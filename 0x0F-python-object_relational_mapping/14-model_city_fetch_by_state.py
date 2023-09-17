#!/usr/bin/python3
"""
Module that connects a python script to a database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def main():
    # Create a database connection using command-line arguments
    db_username, db_password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{db_username}:{db_password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print state-city pairs
    for state, city in session.query(State, City).filter(
            State.id == City.state_id).all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

if __name__ == "__main__":
    main()
