from pydantic import BaseModel, EmailStr, Field


class UserRegistrationModel(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=6)
    isadmin: bool = False


class UserLoginModel(BaseModel):
    email: EmailStr
    password: str


class UserUpdateModel(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=30)
    email: EmailStr | None = None
    password: str | None = Field(None, min_length=6)
    isadmin: bool | None = False

