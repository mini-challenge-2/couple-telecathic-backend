from pydantic import BaseModel
from datetime import datetime
from datetime import date
from app.utils.enum import Type

class SpecialDayBase(BaseModel):
    connection_id: str
    date: date
    description: str
    type: Type
    color: str

class SpecialDay(SpecialDayBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True