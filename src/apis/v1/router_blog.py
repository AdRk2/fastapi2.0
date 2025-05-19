from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from db.repository.blog import create_new_blog
from db.schemas.blog import ShowBlog, CreateBlog
from db.schemas.user import UserCreate, ShowUser
from db.session import get_db


router = APIRouter()

@router.post("/blogs",response_model=ShowBlog,status_code = status.HTTP_201_CREATED)

def create_blog(blog:CreateBlog,db : Session = Depends(get_db)):
    blog = create_new_blog(blog=blog,db=db,author_id =2)

    return blog