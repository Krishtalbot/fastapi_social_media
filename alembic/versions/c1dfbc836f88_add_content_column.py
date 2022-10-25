"""add content column

Revision ID: c1dfbc836f88
Revises: 9a2a8207179a
Create Date: 2022-10-25 21:29:43.819506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1dfbc836f88'
down_revision = '9a2a8207179a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
