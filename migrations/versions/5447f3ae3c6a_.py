"""empty message

Revision ID: 5447f3ae3c6a
Revises: 4c5eb1ca173f
Create Date: 2024-06-13 01:14:27.527345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5447f3ae3c6a'
down_revision = '4c5eb1ca173f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'user_category', ['category_id'], ['category_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_recipe', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###
