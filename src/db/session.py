from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

print("Database URL is ",SQLALCHEMY_DATABASE_URL)

#try-catch errrors
try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
except Exception as e:
    print("Database cannot be up !",e)



SessionLocal = sessionmaker(bind=engine)

def get_db() -> Generator:   #new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()