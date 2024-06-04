from app.db.session import Base
import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Interaction(Base):
    __tablename__ = 'interactions'
    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    sender_id = sa.Column(sa.String(8), sa.ForeignKey('users.id'), nullable=False)
    message_id = sa.Column(sa.Integer, sa.ForeignKey('messages.id'), nullable=False)
    connection_id = sa.Column(sa.Integer, sa.ForeignKey('connections.id'), nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=func.now())

    sender = relationship('User', backref='interactions')
    message = relationship('Message', backref='interactions')
    connection = relationship('Connection', backref='interactions')