"""empty message

Revision ID: 51edc8286a62
Revises: 18b971aeedcd
Create Date: 2022-06-28 16:40:36.505108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51edc8286a62'
down_revision = '18b971aeedcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'post', 'user', ['poster_id'], ['id'])
    op.drop_column('post', 'author')
    op.add_column('reply', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reply', 'post', ['post_id'], ['id'])
    op.add_column('reply_thread', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reply_thread', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reply_thread', type_='foreignkey')
    op.drop_column('reply_thread', 'post_id')
    op.drop_constraint(None, 'reply', type_='foreignkey')
    op.drop_column('reply', 'post_id')
    op.add_column('post', sa.Column('author', sa.VARCHAR(length=100), nullable=True))
    op.drop_constraint(None, 'post', type_='foreignkey')
    # ### end Alembic commands ###
