from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserRegistrationModel(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=6)
    isadmin: bool = False


class UserLoginModel(BaseModel):
    email: EmailStr
    password: str


class UserUpdateModel(BaseModel):
    
    username: Optional[str] = Field(None, min_length=3, max_length=30)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)
    isadmin: Optional[bool] = False

