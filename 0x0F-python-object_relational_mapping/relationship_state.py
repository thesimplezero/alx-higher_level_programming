#!/usr/bin/python3

"""
Module for SQLAlchemy ORM setup and State class definition
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    SQLAlchemy model representing a State.
    
    Attributes:
        id (int): Primary key for the State.
        name (str): The name of the State.
        cities (relationship): One-to-many relationship with City objects.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
