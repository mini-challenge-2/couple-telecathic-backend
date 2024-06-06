from pydantic import BaseModel
from datetime import datetime
from app.utils.enum import Sex

class UserBase(BaseModel):
    apple_id: str
    username: str
    sex: Sex
    email: str
    birth: str
    latitude: float
    longitude: float

class User(UserBase):
    id: str
    created_at: datetime | None = datetime.now()

    class Config:
        orm_mode = True

class UserId(BaseModel):
    id: str

    class Config:
        orm_mode = True