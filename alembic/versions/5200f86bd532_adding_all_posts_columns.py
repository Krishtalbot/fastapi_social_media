"""adding all posts columns

Revision ID: 5200f86bd532
Revises: 9b1fa4aad581
Create Date: 2022-10-25 21:48:55.520667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5200f86bd532'
down_revision = '9b1fa4aad581'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default = 'True')) 
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
