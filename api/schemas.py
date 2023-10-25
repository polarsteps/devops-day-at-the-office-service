from datetime import datetime

from pydantic import BaseModel


class TripCreate(BaseModel):
    name: str
    start_time: datetime
    end_time: datetime


class TripUpdate(BaseModel):
    name: str
    ongoing: bool
    start_time: datetime
    end_time: datetime
