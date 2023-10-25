from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone


class BaseModel(DeclarativeBase):
    pass


class Trip(BaseModel):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    ongoing = Column(Boolean, default=False)
    start_time = Column(DateTime, default=datetime.now(tz=timezone.utc), index=True)
    end_time = Column(DateTime, default=datetime.now(tz=timezone.utc), index=True)
