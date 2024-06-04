from app.db.session import Base
import sqlalchemy as sa
from sqlalchemy.sql import func
import enum

class Gender(enum.Enum):
    female = 0
    male = 1

class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.String(8), primary_key=True, index=True, unique=True)
    apple_id = sa.Column(sa.String(50), unique=True, nullable=False)
    gender = sa.Column(sa.Enum(Gender), nullable=False)
    email = sa.Column(sa.String(50), unique=True, nullable=False)
    birth = sa.Column(sa.Date, nullable=False)
    latitude = sa.Column(sa.Float, nullable=False)
    longitude = sa.Column(sa.Float, nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=func.now())