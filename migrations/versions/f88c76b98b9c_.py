"""empty message

Revision ID: f88c76b98b9c
Revises: 2852b6b58c98
Create Date: 2022-06-28 16:11:55.950092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f88c76b98b9c'
down_revision = '2852b6b58c98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'post', 'user', ['poster_id'], ['id'])
    op.drop_column('post', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author', sa.VARCHAR(length=100), nullable=True))
    op.drop_constraint(None, 'post', type_='foreignkey')
    # ### end Alembic commands ###
