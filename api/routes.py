from datetime import timezone, datetime
from typing import Any

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import Trip
from api.schemas import TripCreate, TripInDB, TripUpdate

router = APIRouter(prefix="/trips")


# @router.post("/")
async def create_trip(trip_data: TripCreate, db: Session = Depends(get_db)) -> TripInDB:
    params = trip_data.model_dump()
    if params["start_time"].date() == datetime.now(timezone.utc).date():
        params["ongoing"] = True
    trip = Trip(**params)
    db.add(trip)
    db.commit()
    return trip


# @router.get("/{trip_id}")
async def get_trip(trip_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
    trip = db.execute(select(Trip).where(Trip.id == trip_id)).scalar_one_or_none()
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {
        "id": trip.id,
        "name": trip.name,
        "ongoing": trip.ongoing,
        "start_time": trip.start_time,
        "end_time": trip.end_time,
    }


# @router.post("/{trip_id}")
async def update_trip(
    trip_id: int, trip_data: TripUpdate, db: Session = Depends(get_db)
) -> TripInDB:
    trip = db.execute(select(Trip).where(Trip.id == trip_id)).scalar_one_or_none()
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")

    for k, v in dict(trip_data).items():
        setattr(trip, k, v)
    db.commit()
    return trip
