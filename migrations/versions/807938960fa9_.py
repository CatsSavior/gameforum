"""empty message

Revision ID: 807938960fa9
Revises: f88c76b98b9c
Create Date: 2022-06-28 16:12:56.886591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '807938960fa9'
down_revision = 'f88c76b98b9c'
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
