#!/usr/bin/python3
""" State class with cities relashionship """

from relationship_city import Base, City
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(Base):
    """
    table : states

    Attributes:
        id : int(state id)
        name : string(state name)
        cities : relashionship(relation to City from State)
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
