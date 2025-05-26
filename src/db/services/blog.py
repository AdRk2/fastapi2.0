from sqlalchemy.orm import Session

from ..models.blog import Blog
from ..schemas.blog import CreateBlog
from ..schemas.blog import UpdateBlog

# CRUD LOGICS
def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(
        id=author_id,
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        author_id=author_id,
        is_active=True,
    )

    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active).all()
    return blogs


def update_blog(id: int, blog: UpdateBlog, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    """"
    if not blog_in_db:
        return {"error":f"Blog with id {id} does not exist"}
    if not blog_in_db.author_id == author_id:                   #new
        return {"error":f"Only the author can modify the blog"}
    """
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db


def delete_blog(id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id)
    """
    if not blog_in_db.first():
        return {"error": f"Could not find blog with id {id}"}
    if not blog_in_db.first().author_id ==author_id:             #new
        return {"error":f"Only the author can delete a blog"}
    """
    blog_in_db.delete()
    db.commit()
    return {"msg": f"deleted blog with id {id}"}
