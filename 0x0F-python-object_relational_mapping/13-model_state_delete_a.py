#!/usr/bin/python3

"""
Module that connects a Python script to a MySQL database, removes states with 'a' in their names using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function to connect to MySQL, remove states with 'a' in their names, and commit the changes.
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
            # Retrieve states with 'a' in their names and delete them
            states = session.query(State).filter(State.name.like('%a%')).all()
            for state in states:
                session.delete(state)
            session.commit()
            print(f"Deleted {len(states)} state(s) with 'a' in their names.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Close the SQLAlchemy session
            session.close()

if __name__ == "__main__":
    main()
