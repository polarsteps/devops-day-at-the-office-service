from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from api.config import settings

engine = create_engine(settings.DATABASE_URL)
DBSession = sessionmaker(bind=engine)


def get_db() -> Session:
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
