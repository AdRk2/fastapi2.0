from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from db.repository.user import create_new_user
from db.schemas.user import UserCreate, ShowUser
from db.session import get_db


router = APIRouter()

@router.post("/",response_model=ShowUser,status_code = status.HTTP_201_CREATED)

def create_user(user:UserCreate,db : Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)

    return user