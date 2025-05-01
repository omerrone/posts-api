"""Add content column to posts table

Revision ID: 4c4f8fdffd4f
Revises: dd9efecad051
Create Date: 2025-05-01 18:45:48.514948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c4f8fdffd4f'
down_revision: Union[str, None] = 'dd9efecad051'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
