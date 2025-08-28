"""add dice column to chart table

Revision ID: f739f3aa8942
Revises: 714ea49bbd33
Create Date: 2025-08-14 13:08:56.094750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f739f3aa8942'
down_revision: Union[str, None] = '714ea49bbd33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('charts', sa.Column('dice', sa.String(), nullable=True))
    op.execute("UPDATE charts SET dice = 'd20' WHERE dice IS NULL")
    op.alter_column('charts', 'dice', nullable=False)


def downgrade() -> None:
    op.drop_column('charts', 'dice')
