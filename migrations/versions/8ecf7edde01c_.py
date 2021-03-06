"""empty message

Revision ID: 8ecf7edde01c
Revises: 16b96ed68fe7
Create Date: 2021-07-13 11:15:38.328227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ecf7edde01c'
down_revision = '16b96ed68fe7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stripe_product', sa.Column('tax', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stripe_product', 'tax')
    # ### end Alembic commands ###
