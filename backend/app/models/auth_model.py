# backend/app/models/auth_model.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class TokenData(BaseModel):
    username: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class UserAuth(BaseModel):
    email: EmailStr
    password: str

class UserCreate(UserAuth):
    username: str
    full_name: Optional[str] = None