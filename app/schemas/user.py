from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str  # ✅ new field


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

class UserOut(UserBase):  # ✅ this was missing
    id: int

    class Config:
        from_attributes = True
