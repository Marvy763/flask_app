"""modification

Revision ID: b6d0e6f16ff9
Revises: b34fac3a99ab
Create Date: 2022-07-06 13:29:40.359269

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b6d0e6f16ff9'
down_revision = 'b34fac3a99ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('res_type', sa.String(length=20), nullable=False),
    sa.Column('res_status', sa.String(length=20), nullable=False),
    sa.Column('res_description', sa.Text(), nullable=False),
    sa.Column('uploader_id', sa.Integer(), nullable=True),
    sa.Column('image_uploaded', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['uploader_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('posts', sa.Column('banner_img', sa.String(length=150), nullable=True))
    op.add_column('users', sa.Column('date_added', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('profile_pic', sa.String(length=150), nullable=True))
    op.drop_column('users', 'data_added')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('data_added', mysql.DATETIME(), nullable=True))
    op.drop_column('users', 'profile_pic')
    op.drop_column('users', 'date_added')
    op.drop_column('posts', 'banner_img')
    op.drop_table('photos')
    # ### end Alembic commands ###
