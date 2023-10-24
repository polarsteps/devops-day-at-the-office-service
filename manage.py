import typer
import uvicorn

from api.core import start_trips, end_trips
from api.main import app
from api.database import engine
from api.models import BaseModel

script = typer.Typer()


@script.command()
def run() -> None:
    """Run the FastAPI server"""
    uvicorn.run(app, host="0.0.0.0", port=8000)


@script.command()
def init_db() -> None:
    """Initialize the database"""
    BaseModel.metadata.create_all(engine)


@script.command()
def start_todays_trips() -> None:
    """Start today's trip"""
    start_trips()


@script.command()
def end_yesterdays_trips() -> None:
    """End Yesterday's trip"""
    end_trips()


if __name__ == "__main__":
    script()
