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

python manage.py init-db
```
### Help
```commandline
python manage.py --help
```
### Running the service

#### API

```
export DATABASE_URL=...
python manage.py run
```

#### Scripts

```commandline
python manage.py start-todays-trips
python manage.py end-yesterdays-trips
```

#### Worker

```
export DATABASE_URL=...
python worker.py
```
