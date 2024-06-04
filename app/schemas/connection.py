from pydantic import BaseModel
from datetime import datetime

class ConnectionBase(BaseModel):
    user_id: str
    partner_id: str

class Connection(ConnectionBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True