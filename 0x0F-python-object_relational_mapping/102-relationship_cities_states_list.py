#!/usr/bin/python3
""" lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa """

from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    statement = session.query(City).order_by(City.id)

    for city in statement:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
