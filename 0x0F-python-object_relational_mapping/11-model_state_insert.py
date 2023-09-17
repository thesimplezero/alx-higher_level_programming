#!/usr/bin/python3

"""
Module that connects a Python script to a MySQL database, adds a new state, and prints its ID using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function to connect to MySQL, add a new state, and print its ID.
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
            # Create the State table if it doesn't exist
            Base.metadata.create_all(engine)

            # Add a new state and commit changes
            new_state = State(name="Louisiana")
            session.add(new_state)
            session.commit()

            # Print the ID of the newly added state
            print(new_state.id)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Close the SQLAlchemy session
            session.close()

if __name__ == "__main__":
    main()
