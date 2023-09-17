#!/usr/bin/python3

"""
Module that connects a Python script to a MySQL database and prints the first state using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function to connect to MySQL, fetch data, and print the first state.
    """
    if __name__ == "__main__":
        # Command-line arguments
        username = argv[1]
        password = argv[2]
        database = argv[3]

        # Create SQLAlchemy engine and session
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Query and print the first state using SQLAlchemy
            state = session.query(State).order_by(State.id).first()
            if state is None:
                print("Nothing")
            else:
                print("{}: {}".format(state.id, state.name))

        except Exception as e:
            print(f"Error executing query: {e}")

        finally:
            # Close the SQLAlchemy session
            session.close()

if __name__ == "__main__":
    main()
