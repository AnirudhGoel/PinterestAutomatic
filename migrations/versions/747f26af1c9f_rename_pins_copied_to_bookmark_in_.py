"""Rename pins_copied to bookmark in PinData

Revision ID: 747f26af1c9f
Revises: 56cc9820012c
Create Date: 2021-05-09 15:17:28.079683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '747f26af1c9f'
down_revision = '56cc9820012c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pin_data', 'pins_copied', new_column_name='bookmark')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pin_data', 'bookmark', new_column_name='pins_copied')
    # ### end Alembic commands ###
