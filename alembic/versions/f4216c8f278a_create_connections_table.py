"""create connections table

Revision ID: f4216c8f278a
Revises: 1adc49d550b6
Create Date: 2024-06-04 09:37:12.276856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4216c8f278a'
down_revision: Union[str, None] = '1adc49d550b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'connections',
        sa.Column('id', sa.Integer, primary_key=True, index=True, unique=True, autoincrement=True),
        sa.Column('user_id', sa.String(8), nullable=False),
        sa.Column('partner_id', sa.String(8), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now())
    )

    op.create_foreign_key(
        "fk_connection_user_id",
        "connections",
        "users",
        ["user_id"],
        ["id"],
        ondelete="cascade",
        onupdate='cascade'
    )

    op.create_foreign_key(
        'fk_connection_partner_id',
        'connections',
        'users',
        ['partner_id'],
        ['id'],
        ondelete='cascade',
        onupdate='cascade'
    )


def downgrade() -> None:
    op.drop_constraint("fk_connection_user_id", "connections", type_="foreignkey")
    op.drop_constraint("fk_connection_partner_id", "connections", type_="foreignkey")
    op.drop_table('connections')
