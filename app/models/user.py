from app.db.session import Base
import sqlalchemy as sa
from sqlalchemy.sql import func
from app.utils.enum import Sex

class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.String(8), primary_key=True, index=True, unique=True)
    apple_id = sa.Column(sa.String(50), unique=True, nullable=False)
    username = sa.Column(sa.String(20), unique=True, nullable=False)
    sex = sa.Column(sa.Enum(Sex), nullable=False)
    email = sa.Column(sa.String(50), unique=True, nullable=False)
    birth = sa.Column(sa.Date, nullable=False)
    latitude = sa.Column(sa.Float, nullable=False)
    longitude = sa.Column(sa.Float, nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=func.now())