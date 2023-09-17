#!/usr/bin/python3

"""
Module that connects a Python script to a MySQL database and finds a state by name using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function to connect to MySQL, fetch data, and find a state by name.
    """
    if __name__ == "__main__":
        # Command-line arguments
        username = argv[1]
        password = argv[2]
        database = argv[3]
        state_name = argv[4]

        # Create SQLAlchemy engine and session
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Query and find a state by name using SQLAlchemy
            state = session.query(State).filter_by(name=state_name).first()
            if state is not None:
                print("{}".format(state.id))
            else:
                print("Not found")

        except Exception as e:
            print(f"Error executing query: {e}")

        finally:
            # Close the SQLAlchemy session
            session.close()

if __name__ == "__main__":
    main()
