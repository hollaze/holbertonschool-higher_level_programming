#!/usr/bin/python3
""" adds the State object “Louisiana” to the database
hbtn_0e_6_usa and print its id when executing """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    louisiana_state = State(name='Louisiana')

    session.add(louisiana_state)
    session.commit()

    louisiana = session.query(State).filter_by(name='Louisiana').first()

    print(louisiana.id)

    session.close()
