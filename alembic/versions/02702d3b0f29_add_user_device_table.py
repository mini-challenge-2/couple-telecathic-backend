"""add user device table

Revision ID: 02702d3b0f29
Revises: ee8e13bd9511
Create Date: 2024-06-07 15:04:13.544844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02702d3b0f29'
down_revision: Union[str, None] = 'ee8e13bd9511'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_devices',
        sa.Column('id', sa.Integer, primary_key=True, index=True, unique=True, autoincrement=True),
        sa.Column('user_id', sa.String(8), nullable=False),
        sa.Column('token', sa.String(100), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now())
    )

    op.create_foreign_key(
        "fk_user_devices_user_id",
        "user_devices",
        "users",
        ["user_id"],
        ["id"],
        ondelete="cascade",
        onupdate='cascade'
    )


def downgrade() -> None:
    op.drop_table('user_devices')
