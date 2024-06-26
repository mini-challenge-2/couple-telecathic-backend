from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    title: str
    content: str

class Message(MessageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True