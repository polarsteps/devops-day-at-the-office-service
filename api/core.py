from datetime import datetime, timedelta

from sqlalchemy import func, update

from api.database import DBSession
from api.models import Trip


def start_trips() -> None:
    """Start all trips using start_trip"""
    db = DBSession()
    db.execute(
        update(Trip).where(func.DATE(Trip.start_time) == func.current_date()).values(ongoing=True))
    db.commit()


def end_trips() -> None:
    """End all yesterday's trip using end_time"""
    db = DBSession()
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    db.execute(update(Trip).where(func.DATE(Trip.end_time) == yesterday).values(ongoing=False))
    db.commit()
