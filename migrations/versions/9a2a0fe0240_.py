"""locale support for user

Revision ID: 9a2a0fe0240
Revises: ad05b7557e4
Create Date: 2014-10-12 23:18:40.859143

"""

# revision identifiers, used by Alembic.
revision = '9a2a0fe0240'
down_revision = 'ad05b7557e4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('locale', sa.String(length=2), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'locale')
    ### end Alembic commands ###
