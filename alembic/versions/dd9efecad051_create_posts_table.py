"""create posts table

Revision ID: dd9efecad051
Revises: 
Create Date: 2025-05-01 18:31:58.654298

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd9efecad051'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts", sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String, nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
