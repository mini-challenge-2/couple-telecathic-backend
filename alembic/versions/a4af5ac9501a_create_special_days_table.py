"""create special_days table

Revision ID: a4af5ac9501a
Revises: 3e62a41eba92
Create Date: 2024-06-04 09:50:01.742504

"""
from typing import Sequence, Union

import enum
from alembic import op
import sqlalchemy as sa
from app.utils.enum import Type

# revision identifiers, used by Alembic.
revision: str = 'a4af5ac9501a'
down_revision: Union[str, None] = '3e62a41eba92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'special_days',
        sa.Column('id', sa.Integer, primary_key=True, index=True, unique=True, autoincrement=True),
        sa.Column('connection_id', sa.Integer, nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('description', sa.String(255), nullable=False),
        sa.Column('type', sa.Enum(Type), nullable=False),
        sa.Column('color', sa.String(8), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    op.create_foreign_key(
        "fk_special_days_connections_id",
        "special_days",
        "connections",
        ["connection_id"],
        ["id"],
        ondelete="cascade",
        onupdate='cascade'
    )


def downgrade() -> None:
    op.drop_constraint("fk_special_days_connections_id", "special_days", type_="foreignkey")
    op.drop_table('special_days')
