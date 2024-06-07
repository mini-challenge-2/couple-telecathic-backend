from app.db.session import Base
import sqlalchemy as sa
from sqlalchemy.sql import func
from app.utils.enum import Sex
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.String(8), primary_key=True, index=True, unique=True)
    apple_id = sa.Column(sa.String(50), unique=True, nullable=False)
    username = sa.Column(sa.String(20), unique=True, nullable=False)
    sex = sa.Column(sa.Enum(Sex), nullable=False)
    email = sa.Column(sa.String(50), unique=True, nullable=False)
    birth = sa.Column(sa.String(50), nullable=False)
    latitude = sa.Column(sa.Float, nullable=False)
    longitude = sa.Column(sa.Float, nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=func.now())

class UserDevice(Base):
    __tablename__ = 'user_devices'
    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    user_id = sa.Column(sa.String(8), sa.ForeignKey('users.id', ondelete='cascade', onupdate='cascade'), nullable=False)
    token = sa.Column(sa.String(100), nullable=False)

    user = relationship('User', backref='user_devices', foreign_keys=[user_id])