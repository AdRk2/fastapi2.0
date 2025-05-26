"""create user and blog table migrations

Revision ID: 642a9a86906e
Revises:
Create Date: 2025-05-19 13:22:48.619781

"""
from typing import Sequence
from typing import Union


# revision identifiers, used by Alembic.
revision: str = "1ba722b0c1c2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
