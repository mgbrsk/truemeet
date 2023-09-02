"""create user table

Revision ID: 317f2d7de797
Revises: 
Create Date: 2023-09-02 17:41:02.874715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '317f2d7de797'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(255), unique=True, nullable=False),
        sa.Column('user_id', sa.String(255), unique=True, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('user')
