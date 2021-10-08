#!/usr/bin/python3
""" select state as an argument and print its id,
if not exists print 'Not found' """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter_by(name=sys.argv[4]).first()

    if state is None:
        print('Not found')
    else:
        print(state.id)

    session.close()
