from pydantic import BaseModel


class TripCreate(BaseModel):
    name: str


class TripUpdate(BaseModel):
    name: str
    ongoing: bool
