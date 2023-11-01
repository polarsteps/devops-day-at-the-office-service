# Trips Service

Day at the office assignment - DevOps Engineer

This is a very simple service for querying and saving trips.

### Requirements

- Python 3 (>= 3.10)

### Setting up

```bash
pip install -r requirements.txt

# For local test environments:
export DATABASE_URL="sqlite:///./sqlite.db"
# For other environments:
# export DATABASE_URL = "postgresql://user:password@dbserver/db"
```

### Help

```bash
python manage.py --help
```

### Running the service

#### API

```bash
export DATABASE_URL=...
python manage.py run
```

#### Scripts

These two scripts need to be run once a day:

```bash
python manage.py start-todays-trips
python manage.py end-yesterdays-trips
```


### Testing

For tests, the `DATABASE_URL` is hardcoded in tests to use a sqlite database.


```bash
pytest
```
