"""empty message

Revision ID: 2d36e304fc73
Revises: None
Create Date: 2014-09-29 21:24:21.638678

"""

# revision identifiers, used by Alembic.
revision = '2d36e304fc73'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recently_added',
    sa.Column('item_id', sa.Text(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('debug', sa.Text(), nullable=True),
    sa.Column('file', sa.Integer(), nullable=True),
    sa.Column('twitter', sa.Integer(), nullable=True),
    sa.Column('growl', sa.Integer(), nullable=True),
    sa.Column('prowl', sa.Integer(), nullable=True),
    sa.Column('GNTP', sa.Integer(), nullable=True),
    sa.Column('EMAIL', sa.Integer(), nullable=True),
    sa.Column('pushover', sa.Integer(), nullable=True),
    sa.Column('boxcar', sa.Integer(), nullable=True),
    sa.Column('boxcar_v2', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_table('grouped',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Text(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('user', sa.Text(), nullable=True),
    sa.Column('platform', sa.Text(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('orig_title', sa.Text(), nullable=True),
    sa.Column('orig_title_ep', sa.Text(), nullable=True),
    sa.Column('episode', sa.Integer(), nullable=True),
    sa.Column('season', sa.Integer(), nullable=True),
    sa.Column('year', sa.Text(), nullable=True),
    sa.Column('rating', sa.Text(), nullable=True),
    sa.Column('genre', sa.Text(), nullable=True),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('notified', sa.Integer(), nullable=True),
    sa.Column('stopped', sa.DateTime(), nullable=True),
    sa.Column('paused', sa.DateTime(), nullable=True),
    sa.Column('paused_counter', sa.Integer(), nullable=True),
    sa.Column('xml', sa.Text(), nullable=True),
    sa.Column('ip_address', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('processed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Text(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('user', sa.Text(), nullable=True),
    sa.Column('platform', sa.Text(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('orig_title', sa.Text(), nullable=True),
    sa.Column('orig_title_ep', sa.Text(), nullable=True),
    sa.Column('episode', sa.Integer(), nullable=True),
    sa.Column('season', sa.Integer(), nullable=True),
    sa.Column('year', sa.Text(), nullable=True),
    sa.Column('rating', sa.Text(), nullable=True),
    sa.Column('genre', sa.Text(), nullable=True),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('notified', sa.Integer(), nullable=True),
    sa.Column('stopped', sa.DateTime(), nullable=True),
    sa.Column('paused', sa.DateTime(), nullable=True),
    sa.Column('paused_counter', sa.Integer(), nullable=True),
    sa.Column('xml', sa.Text(), nullable=True),
    sa.Column('ip_address', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('processed')
    op.drop_table('user')
    op.drop_table('grouped')
    op.drop_table('recently_added')
    ### end Alembic commands ###
