from sqlalchemy.orm import Session

from db.schemas.blog import CreateBlog
from db.services.blog import create_new_blog
from tests.utils.user import create_random_user


def create_random_blog(db:Session):
    blog = CreateBlog(title="first_blog",slug="first_blog",content="test try all use case")
    user = create_random_user(db=db)
    blog = create_new_blog(blog,db,author_id=user.id)
    return blog