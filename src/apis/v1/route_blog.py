from typing import List

from db.schemas.blog import CreateBlog, UpdateBlog
from db.schemas.blog import ShowBlog
from db.services.blog import create_new_blog
from db.services.blog import delete_blog
from db.services.blog import list_blogs
from db.services.blog import retrieve_blog
from db.services.blog import update_blog
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status


router = APIRouter()

# display CRUD ROUTES
@router.post("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog


@router.get("/blogs/{id}", response_model=ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id: {id} does not exist",
        )
    return blog


@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs


@router.put("/blogs/{id}", response_model=ShowBlog)
def update_a_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog, db=db)
    if isinstance(blog, dict):
        raise HTTPException(
            detail=blog.get("error"),
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.delete("/blogs/{id}")
def delete_a_blog(id: int, db: Session = Depends(get_db)):
    message = delete_blog(id=id, db=db)
    if message.get("error"):
        raise HTTPException(
            detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"msg": f"Successfully deleted blog with id {id}"}
