"""create users table

Revision ID: 1adc49d550b6
Revises: 
Create Date: 2024-06-04 09:28:54.063281

"""
from typing import Sequence, Union

import enum
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1adc49d550b6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

class Sex(enum.Enum):
    female = 0
    male = 1

def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column('id', sa.String(8), primary_key=True, index=True, unique=True),
        sa.Column('apple_id', sa.String(50), unique=True, nullable=False),
        sa.Column('username', sa.String(20), unique=True, nullable=False),
        sa.Column('sex', sa.Enum(Sex), nullable=False),
        sa.Column('email', sa.String(50), unique=True, nullable=False),
        sa.Column('birth', sa.Date, nullable=False),
        sa.Column('latitude', sa.Float, nullable=False),
        sa.Column('longitude', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("users")
