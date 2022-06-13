"""empty message

Revision ID: f728f0b31302
Revises: 8624d15c7edb
Create Date: 2022-06-13 18:51:16.414019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f728f0b31302'
down_revision = '8624d15c7edb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teacher', 'avatar',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teacher', 'avatar',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
