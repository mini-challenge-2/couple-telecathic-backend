from pydantic import BaseModel
from datetime import datetime

class InteractionBase(BaseModel):
    sender_id: str
    message_id: int
    connection_id: int

class Interaction(InteractionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True