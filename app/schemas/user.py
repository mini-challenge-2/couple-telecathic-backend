from pydantic import BaseModel
from datetime import datetime
from datetime import date
from app.utils.enum import Sex

class UserBase(BaseModel):
    apple_id: str
    gender: Sex
    email: str
    birth: date
    latitude: float
    longitude: float

class User(UserBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True