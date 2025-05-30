from db.schemas.user import ShowUser
from db.schemas.user import UserCreate
from db.services.user import create_new_user
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status


router = APIRouter()


@router.post("/users", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)

    return user
