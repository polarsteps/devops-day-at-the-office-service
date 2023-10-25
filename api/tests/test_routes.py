from typing import Any
from fastapi.testclient import TestClient


def test_create_trip(client: TestClient):
    data = {
        "name": "test",
        "start_time": "2021-01-01T00:00:00Z",
        "end_time": "2021-01-01T00:00:00Z",
    }
    response = client.post("/trips/", json=data)

    assert response.status_code == 200
    data = response.json()

    assert data["id"]
    assert data["name"] == "test"
    assert data["ongoing"] is False


def test_get_trip(client: TestClient, trip: dict[str, Any]):
    id = trip["id"]
    response = client.get(f"/trips/{id}")
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == id
    assert data["name"] == "test"
    assert data["ongoing"] is False


def test_update_trip(client: TestClient, trip: dict[str, Any]):
    id = trip["id"]

    data = {**trip, "name": "test2", "ongoing": not trip["ongoing"]}
    response = client.post(f"/trips/{id}", json=data)
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["id"] == id
    assert data["name"] == "test2"
    assert data["ongoing"] is not trip["ongoing"]
