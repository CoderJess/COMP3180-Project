"""empty message

Revision ID: a4395199347a
Revises: 51e8d7304ff6
Create Date: 2025-05-06 20:11:26.009397

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a4395199347a'
down_revision = '51e8d7304ff6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('user')
    with op.batch_alter_table('favourite', schema=None) as batch_op:
        batch_op.alter_column('user_id_fk',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('fav_user_id_fk',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.create_foreign_key(None, 'users', ['user_id_fk'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['fav_user_id_fk'], ['id'])

    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('user_id_fk',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=200),
               existing_nullable=True)
        batch_op.alter_column('parish',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('biography',
               existing_type=sa.VARCHAR(length=600),
               type_=sa.String(length=200),
               existing_nullable=True)
        batch_op.alter_column('sex',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=10),
               existing_nullable=True)
        batch_op.alter_column('race',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=10),
               existing_nullable=True)
        batch_op.alter_column('fav_cuisine',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=30),
               existing_nullable=True)
        batch_op.alter_column('fav_colour',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=15),
               existing_nullable=True)
        batch_op.alter_column('fav_school_subject',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.drop_constraint('profile_user_id_fk_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id_fk'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('profile_user_id_fk_fkey', 'user', ['user_id_fk'], ['id'])
        batch_op.alter_column('fav_school_subject',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=80),
               existing_nullable=True)
        batch_op.alter_column('fav_colour',
               existing_type=sa.String(length=15),
               type_=sa.VARCHAR(length=80),
               existing_nullable=True)
        batch_op.alter_column('fav_cuisine',
               existing_type=sa.String(length=30),
               type_=sa.VARCHAR(length=80),
               existing_nullable=True)
        batch_op.alter_column('race',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('sex',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
        batch_op.alter_column('biography',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=600),
               existing_nullable=True)
        batch_op.alter_column('parish',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=80),
               existing_nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('user_id_fk',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_column('created_at')

    with op.batch_alter_table('favourite', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('fav_user_id_fk',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id_fk',
               existing_type=sa.INTEGER(),
               nullable=True)

    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('photo', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('date_joined', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('username', name='user_username_key')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
