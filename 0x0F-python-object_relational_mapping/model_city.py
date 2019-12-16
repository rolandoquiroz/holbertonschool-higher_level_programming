#!/usr/bin/python3
"""
File that contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    class City inherits from Base
    """
    """
    links to the MySQL table cities
    """
    __tablename__ = 'cities'
    """
    class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    """
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    """
    class attribute name that represents a column of a string
    with maximum 128 characters and can’t be null
    """
    name = Column(String(128), nullable=False)

    """
    class attribute state_id that represents a column of an integer,
    can’t be null and is a foreign key to states.id
    """
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
