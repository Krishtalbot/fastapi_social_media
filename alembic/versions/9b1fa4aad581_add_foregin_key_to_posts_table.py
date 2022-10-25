"""add foregin key to posts table

Revision ID: 9b1fa4aad581
Revises: 256575f081ca
Create Date: 2022-10-25 21:39:30.408865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b1fa4aad581'
down_revision = '256575f081ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fkey', source_table = "posts", referent_table= "users", local_cols = ['owner_id'],
    remote_cols = ['id'], ondelete = "CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraints('posts_users_fkey', table_name= 'posts')
    op.drop_column('posts', 'owner_id')
    pass
