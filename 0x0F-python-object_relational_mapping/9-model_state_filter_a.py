#!/usr/bin/python3

"""
Module that connects a Python script to a MySQL database and prints states containing 'a' using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function to connect to MySQL, fetch data, and print states containing 'a'.
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
            # Query and print states containing 'a' using SQLAlchemy
            for state in session.query(State).order_by(State.id):
                if "a" in state.name:
                    print("{}: {}".format(state.id, state.name))

        except Exception as e:
            print(f"Error executing query: {e}")

        finally:
            # Close the SQLAlchemy session
            session.close()

if __name__ == "__main__":
    main()
