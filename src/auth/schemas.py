from pydantic import (
    BaseModel,
    EmailStr,
    Field,
)


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=6)


class UserCreate(UserBase):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRegisterOut(BaseModel):
    message: str


# class UserOut(BaseModel):
#     id: UUID
#     username: str
#     email: EmailStr
#     is_verified: bool
#     created_at: datetime
#     updated_at: datetime

#     model_config = ConfigDict(from_attributes=True)
