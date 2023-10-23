from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import BaseModel


def init_db(db_url: str) -> Session:
    engine = create_engine(db_url)
    DBSession = sessionmaker(bind=engine)
    BaseModel.metadata.create_all(engine)
    return DBSession


def db_getter(DBSession) -> Callable[[], Session]:
    def get_db() -> Session:
        db = DBSession()
        try:
            yield db
        finally:
            db.close()

    return get_db
