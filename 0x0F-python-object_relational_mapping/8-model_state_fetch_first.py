#!/usr/bin/python3
"""print first state"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
import sys
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).get(1)

    if state is None:
        print("Nothing")

    print("{}: {}".format(state.id, state.name))

    session.close()
