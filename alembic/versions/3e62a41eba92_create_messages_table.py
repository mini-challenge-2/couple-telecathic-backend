"""create messages table

Revision ID: 3e62a41eba92
Revises: f4216c8f278a
Create Date: 2024-06-04 09:44:31.379209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e62a41eba92'
down_revision: Union[str, None] = 'f4216c8f278a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer, primary_key=True, index=True, unique=True, autoincrement=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('content', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table('messages')
