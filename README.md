# Trips Service

Day at the office assignment - DevOps Engineer

This is a very simple service for querying and saving trips.

### Requirements

- Python 3 (>= 3.10)

### Setting up

```
pip install -r requirements.txt

# For local test environments:
export DATABASE_URL="sqlite:///./sqlite.db"
# For other environments:
# export DATABASE_URL = "postgresql://user:password@dbserver/db"

python api.py init
```

### Running the service

#### API

```
export DATABASE_URL=...
uvicorn api:app --reload
```

#### Worker

```
export DATABASE_URL=...
python worker.py
```
