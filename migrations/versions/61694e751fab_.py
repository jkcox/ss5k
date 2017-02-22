"""empty message

Revision ID: 61694e751fab
Revises: 5e6a47c59a87
Create Date: 2017-02-21 22:46:43.489770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61694e751fab'
down_revision = '5e6a47c59a87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wanted_car', sa.Column('color', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wanted_car', 'color')
    # ### end Alembic commands ###