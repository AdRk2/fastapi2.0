from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from db.repository.blog import create_new_blog, retrieve_blog, list_blogs
from db.schemas.blog import ShowBlog, CreateBlog
from db.session import get_db


router = APIRouter()

@router.post("/blogs",response_model=ShowBlog,status_code = status.HTTP_201_CREATED)

def create_blog(blog:CreateBlog,db : Session = Depends(get_db)):
    blog = create_new_blog(blog=blog,db=db,author_id =5) ##fix the value dynamically
    return blog

@router.get("/blogs/{id}",response_model=ShowBlog)
def get_blog (id:int , db:Session = Depends(get_db)):
    blog = retrieve_blog(id=id,db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id: {id} does not exist")
    return blog

@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs