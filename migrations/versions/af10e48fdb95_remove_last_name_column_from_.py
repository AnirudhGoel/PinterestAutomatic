"""Remove last_name column from PinterestData

Revision ID: af10e48fdb95
Revises: 15bc07f4f165
Create Date: 2021-04-25 11:50:35.771261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af10e48fdb95'
down_revision = '15bc07f4f165'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pinterest_data', 'last_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pinterest_data', sa.Column('last_name', sa.VARCHAR(length=300), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
