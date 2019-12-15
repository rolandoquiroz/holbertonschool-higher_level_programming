#!/usr/bin/python3
"""
File that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class State inherits from Base
    """
    """
    links to the MySQL table states
    """
    __tablename__ = 'states'
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
