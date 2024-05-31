"""empty message

Revision ID: 313fdb77a075
Revises: e7e0ab3a30ac
Create Date: 2024-05-31 23:29:03.946060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '313fdb77a075'
down_revision = 'e7e0ab3a30ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_recipe_ingredient',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('user_recipe_ingredient_id', sa.Integer(), nullable=False),
    sa.Column('calories', sa.Float(), nullable=True),
    sa.Column('protein_in_grams', sa.Float(), nullable=True),
    sa.Column('carbohydrates_in_grams', sa.Float(), nullable=True),
    sa.Column('fats_in_grams', sa.Float(), nullable=True),
    sa.Column('sodium_in_mg', sa.Float(), nullable=True),
    sa.Column('cholestorol_in_mg', sa.Float(), nullable=True),
    sa.Column('fiber_in_grams', sa.Float(), nullable=True),
    sa.Column('sugars_in_grams', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['user_recipe.recipe_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_recipe_ingredient_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_recipe_ingredient')
    # ### end Alembic commands ###
