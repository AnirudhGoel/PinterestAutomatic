"""Add Payments model

Revision ID: 51e8a819ee05
Revises: 935fc790413c
Create Date: 2021-05-13 14:29:17.223064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51e8a819ee05'
down_revision = '935fc790413c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('amount_received', sa.Integer(), server_default='0', nullable=True),
    sa.Column('currency', sa.String(length=3), nullable=False, server_default=''),
    sa.Column('pins_bought', sa.Integer(), server_default='0', nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payments_user_id'), 'payments', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_payments_user_id'), table_name='payments')
    op.drop_table('payments')
    # ### end Alembic commands ###