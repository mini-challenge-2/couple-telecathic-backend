"""messages seeder

Revision ID: ee8e13bd9511
Revises: f8b9edc06a95
Create Date: 2024-06-06 09:26:35.340148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.models.message import Message


# revision identifiers, used by Alembic.
revision: str = 'ee8e13bd9511'
down_revision: Union[str, None] = 'f8b9edc06a95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    messages = [
        {
            'title': 'Thinking about You ☺️',
            'content': 'Hi Babe, I’m thinking about You right now'
        },
        {
            'title': 'Don’t forget to Eat 🍽️',
            'content': 'Don’t let your stomach empty Babe<3'
        },
        {
            'title': 'Want to Meet You 🤗',
            'content': 'I really miss you right now. Hope we can meet soon'
        },
        {
            'title': 'Be Right Back 🥺',
            'content': 'Babe, I will be unresponsive for a while. Gonna be right back ASAP'
        }
    ]

    for data in messages:
        message = Message(**data)
        session.add(message)
        session.flush()

def downgrade() -> None:
    pass
