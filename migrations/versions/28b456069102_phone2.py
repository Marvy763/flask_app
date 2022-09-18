"""phone2

Revision ID: 28b456069102
Revises: 3f6a31f94ccf
Create Date: 2022-07-22 15:05:16.748247

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '28b456069102'
down_revision = '3f6a31f94ccf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone', sa.String(length=20), nullable=True))
    op.drop_column('users', 'phone1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone1', mysql.VARCHAR(length=20), nullable=True))
    op.drop_column('users', 'phone')
    # ### end Alembic commands ###
