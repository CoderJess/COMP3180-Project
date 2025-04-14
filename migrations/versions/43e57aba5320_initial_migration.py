"""initial migration

Revision ID: 43e57aba5320
Revises: 
Create Date: 2025-04-14 15:58:07.193196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43e57aba5320'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('photo', sa.String(length=200), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('fav_user_id', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['fav_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'fav_user_id', name='unique_favourite')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('parish', sa.String(length=50), nullable=False),
    sa.Column('biography', sa.Text(), nullable=False),
    sa.Column('sex', sa.String(length=20), nullable=False),
    sa.Column('race', sa.String(length=50), nullable=False),
    sa.Column('birth_year', sa.Integer(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('fav_cuisine', sa.String(length=50), nullable=False),
    sa.Column('fav_colour', sa.String(length=30), nullable=False),
    sa.Column('fav_school_subject', sa.String(length=50), nullable=False),
    sa.Column('political', sa.Boolean(), nullable=False),
    sa.Column('religious', sa.Boolean(), nullable=False),
    sa.Column('family_oriented', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.drop_table('favourites')
    op.drop_table('users')
    # ### end Alembic commands ###
