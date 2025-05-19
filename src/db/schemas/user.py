from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email : EmailStr
    password : str= Field(..., min_lenght=4)