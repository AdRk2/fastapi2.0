from typing import Generator

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL ="postgresql://stg:adam@172.20.0.2:5432/blogdb"
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# try-catch errrors
try:
    SessionLocal = sessionmaker(bind=engine)
except Exception as e:
    print("Database cannot be up !", e)



def get_db() -> Generator:  # new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
