"""empty message

Revision ID: 6cecfa349d58
Revises: d07deee49aa1
Create Date: 2021-07-13 11:33:03.375653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cecfa349d58'
down_revision = 'd07deee49aa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stripe_product', sa.Column('stripe_product_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stripe_product', 'stripe_product_id')
    # ### end Alembic commands ###
