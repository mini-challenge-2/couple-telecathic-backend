from app.db.session import Base
import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Connection(Base):
    __tablename__ = 'connections'
    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    user_id = sa.Column(sa.String(8), sa.ForeignKey('users.id'), nullable=False)
    partner_id = sa.Column(sa.String(8), sa.ForeignKey('users.id'), nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=func.now())

    user = relationship('User', backref='connections_as_user', foreign_keys=[user_id])
    partner = relationship('User', backref='connections_as_partner', foreign_keys=[partner_id])
