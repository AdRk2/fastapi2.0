import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://stg:adam@db:5432/blogdb"  # Use service name

def create_db_engine():
    max_retries = 5
    wait_seconds = 5
    for retry in range(max_retries):
        try:
            engine = create_engine(DATABASE_URL)
            engine.connect()  # Try to connect
            print("Database connection successful!")
            return engine
        except OperationalError as e:
            print(f"Connection failed (attempt {retry + 1}/{max_retries}): {e}")
            if retry < max_retries - 1:
                time.sleep(wait_seconds)
            else:
                raise  # Re-raise the exception after max retries

engine = create_db_engine()
# Now you can use the 'engine' object to interact with the database

