from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    pass


class Trip(BaseModel):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    ongoing = Column(Boolean, default=False)
