#!/usr/bin/python3
"""
Script that changes the name of a State object
from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    """ This won't be run when imported """

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    state_id_found = session.query(State).filter_by(id=2).first()

    if state_id_found:
        state_id_found.name = "New Mexico"
        session.commit()

    session.close()
