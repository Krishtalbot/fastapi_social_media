"""add user table

Revision ID: 256575f081ca
Revises: c1dfbc836f88
Create Date: 2022-10-25 21:33:09.109248

"""
from sqlite3 import Timestamp
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '256575f081ca'
down_revision = 'c1dfbc836f88'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
