"""create interactions table

Revision ID: f8b9edc06a95
Revises: a4af5ac9501a
Create Date: 2024-06-04 09:53:56.940462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8b9edc06a95'
down_revision: Union[str, None] = 'a4af5ac9501a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'interactions',
        sa.Column('id', sa.Integer, primary_key=True, index=True, unique=True, autoincrement=True),
        sa.Column('sender_id', sa.String(8), nullable=False),
        sa.Column('message_id', sa.Integer, nullable=False),
        sa.Column('connection_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    op.create_foreign_key(
        "fk_interactions_sender_id",
        "interactions",
        "users",
        ["sender_id"],
        ["id"],
        ondelete="cascade",
        onupdate='cascade'
    )

    op.create_foreign_key(
        'fk_interactions_message_id',
        'interactions',
        'messages',
        ['message_id'],
        ['id'],
        ondelete='cascade',
        onupdate='cascade'
    )
    
    op.create_foreign_key(
        'fk_interactions_connection_id',
        'interactions',
        'connections',
        ['connection_id'],
        ['id'],
        ondelete='cascade',
        onupdate='cascade'
    )


def downgrade() -> None:
    op.drop_constraint("fk_interactions_sender_id", "interactions", type_="foreignkey")
    op.drop_constraint("fk_interactions_message_id", "interactions", type_="foreignkey")
    op.drop_constraint("fk_interactions_connection_id", "interactions", type_="foreignkey")
    op.drop_table('interactions')
