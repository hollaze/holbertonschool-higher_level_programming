#!/usr/bin/python3
""" City class """

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class City(Base):
    """
    table: cities

    Attributes:
        id : int(city id)
        name : string(city name)
        state_id : string(state id)
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
