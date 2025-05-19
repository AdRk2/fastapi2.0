from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from db.services.blog import create_new_blog, retrieve_blog, list_blogs, update_blog, delete_blog
from db.schemas.blog import ShowBlog, CreateBlog
from db.session import get_db


router = APIRouter()

@router.post("/blogs",response_model=ShowBlog,status_code = status.HTTP_201_CREATED)

def create_blog(blog:CreateBlog,db : Session = Depends(get_db)):
    blog = create_new_blog(blog=blog,db=db,author_id = blog.author_id) ##fix the value dynamically
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

@router.put("/blogs/{id}",response_model=ShowBlog)
def update_a_blog(id:int,blog:CreateBlog,db:Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog,author_id=1,db=db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} does not exist"
        )
    return blog

@router.delete("/delete/{id}")
def delete_a_blog(id:int,db:Session = Depends(get_db)):
    message = delete_blog(id=id,db=db)
    if message.get("error"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Blog with id: {id} does not exist")
    else:
        return {"message":"blog deleted successfully"}
