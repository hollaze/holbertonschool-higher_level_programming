#!/usr/bin/python3
""" prints states, id, cities """

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    statement = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)

    for state, city in statement:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
