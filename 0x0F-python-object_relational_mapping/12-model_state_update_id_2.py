#!/usr/bin/python3

"""
Module that connects a Python script to a MySQL database, updates a state's name, and commits the change using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function to connect to MySQL, update a state's name, and commit the change.
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
            # Update the state's name with id=2 to "New Mexico" and commit changes
            state = session.query(State).filter_by(id=2).first()
            if state:
                state.name = "New Mexico"
                session.commit()
            else:
                print("State with id=2 not found.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Close the SQLAlchemy session
            session.close()

if __name__ == "__main__":
    main()
