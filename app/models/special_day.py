from app.db.session import Base
import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.utils.enum import Type

class SpecialDay(Base):
    __tablename__ = 'special_days'
    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    connection_id = sa.Column(sa.Integer, sa.ForeignKey('connections.id'), nullable=False)
    date = sa.Column(sa.Date, nullable=False)
    description = sa.Column(sa.String(255), nullable=False)
    type = sa.Column(sa.Enum(Type), nullable=False)
    color = sa.Column(sa.String(8), nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=func.now())

    connection = relationship('Connection', backref='special_days')