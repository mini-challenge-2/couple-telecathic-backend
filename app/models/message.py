from app.db.session import Base
import sqlalchemy as sa
from sqlalchemy.sql import func

class Message(Base):
    __tablename__ = 'messages'
    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    title = sa.Column(sa.String(50), nullable=False)
    content = sa.Column(sa.String(255), nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=func.now())