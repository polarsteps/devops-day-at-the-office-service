from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from api.config import settings
from api.models import BaseModel

engine = create_engine(settings.DATABASE_URL)
DBSession = sessionmaker(bind=engine)


def init_db(db_url: str) -> Session:
    engine = create_engine(db_url)
    DBSession = sessionmaker(bind=engine)
    BaseModel.metadata.create_all(engine)
    return DBSession


def get_db() -> Session:
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
