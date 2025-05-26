from db.schemas.user import UserCreate
from db.services.user import create_new_user
from sqlalchemy.orm import Session


def create_random_user(db: Session):
    user = UserCreate(email="ping@fastapitutorial.com", password="ping123456789")
    user = create_new_user(user=user, db=db)
    return user
