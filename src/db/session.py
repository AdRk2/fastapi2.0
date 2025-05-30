from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

##docker environnment base
#SQLALCHEMY_DATABASE_URL ="postgresql://stg:adam@db:5432/blogdb"

SQLALCHEMY_DATABASE_URL = "postgresql://devadmin:ijustwanttolog2%40@d:5432/postgres"
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
