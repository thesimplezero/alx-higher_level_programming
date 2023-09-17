#!/usr/bin/python3

"""
Module for SQLAlchemy ORM setup and City class definition
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """
    SQLAlchemy model representing a City.

    Attributes:
        id (int): Primary key for the City.
        name (str): The name of the City.
        state_id (int): Foreign key reference to the associated State.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
