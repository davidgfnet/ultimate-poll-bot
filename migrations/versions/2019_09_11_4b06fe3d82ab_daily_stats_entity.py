"""Daily stats entity

Revision ID: 4b06fe3d82ab
Revises: 0a1d3e362730
Create Date: 2019-09-11 21:47:05.890372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b06fe3d82ab'
down_revision = '0a1d3e362730'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'daily_statistic',
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('votes', sa.Integer(), nullable=False),
        sa.Column('callback_calls', sa.Integer(), nullable=False),
        sa.Column('new_users', sa.Integer(), nullable=False),
        sa.Column('created_polls', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daily_statistic')
    # ### end Alembic commands ###
