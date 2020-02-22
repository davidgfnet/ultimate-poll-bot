"""Add last updated to user

Revision ID: f1c0140a53d4
Revises: 21574a420c32
Create Date: 2020-02-23 17:22:38.578437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1c0140a53d4'
down_revision = '21574a420c32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('poll', 'current_date')
    op.add_column('user', sa.Column('last_update', sa.DateTime()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_update')
    op.add_column('poll', sa.Column('current_date', sa.DATE(), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
