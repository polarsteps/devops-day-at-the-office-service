import os

from fastapi import FastAPI

from database import init_db, db_getter
from routes import create_routes


def create_app(db_url: str) -> FastAPI:
    app = FastAPI()
    DBSession = init_db(db_url)
    get_db = db_getter(DBSession)
    create_routes(app, get_db)
    return app


app = create_app(os.environ["DATABASE_URL"])
