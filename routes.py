from typing import Callable

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Trip
from schemas import TripCreate, TripUpdate


def create_routes(app: FastAPI, get_db: Callable[[], Session]) -> None:
    @app.post("/trips")
    async def create_trip(trip_data: TripCreate, db: Session = Depends(get_db)):
        db.add(Trip(name=trip_data.name))
        db.commit()
        return "ok"

    @app.get("/trips/{trip_id}")
    async def get_trip(trip_id: int, db: Session = Depends(get_db)):
        trip = db.execute(select(Trip).where(Trip.id == trip_id)).scalar_one_or_none()
        if trip is None:
            raise HTTPException(status_code=404, detail="Trip not found")
        return {
            "id": trip.id,
            "name": trip.name,
            "ongoing": trip.ongoing,
        }

    @app.post("/trips/{trip_id}")
    async def update_trip(
        trip_id: int, trip_data: TripUpdate, db: Session = Depends(get_db)
    ):
        trip = db.execute(select(Trip).where(Trip.id == trip_id)).scalar_one_or_none()
        if trip is None:
            raise HTTPException(status_code=404, detail="Trip not found")

        for k, v in dict(trip_data).items():
            setattr(trip, k, v)
        db.commit()
        return "ok"
