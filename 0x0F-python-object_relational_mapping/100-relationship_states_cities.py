#!/usr/bin/python3
""" prints states, id, cities """

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
    state = State(name="California")
    # Add state from city with session
    city = City(name="San Francisco", state=state)

    session.add(city)
    session.commit()

    session.close()
