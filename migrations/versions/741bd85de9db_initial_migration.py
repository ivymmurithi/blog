"""Initial Migration

Revision ID: 741bd85de9db
Revises: 49cd42f46735
Create Date: 2022-02-12 14:13:42.844474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '741bd85de9db'
down_revision = '49cd42f46735'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
