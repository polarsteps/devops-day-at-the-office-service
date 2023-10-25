import os
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="session", autouse=True)
def set_env():
    os.environ["DATABASE_URL"] = "sqlite:///./sqlite.db"


@pytest.fixture(scope="session", autouse=True)
def init_db(set_env):
    from api.models import BaseModel
    from api.database import engine

    BaseModel.metadata.create_all(engine)


@pytest.fixture
def client():
    from api.main import app

    return TestClient(app)


@pytest.fixture
def trip(client):
    data = {
        "name": "test",
        "start_time": "2021-01-01T00:00:00Z",
        "end_time": "2021-01-01T00:00:00Z",
    }

    response = client.post("/trips/", json=data)
    return response.json()
