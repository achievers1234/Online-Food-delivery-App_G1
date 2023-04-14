"""second migration

Revision ID: 6f0a673f5542
Revises: 
Create Date: 2023-03-21 14:00:49.240540

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6f0a673f5542'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('addresses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_by', sa.Integer(), nullable=True))
        batch_op.drop_constraint('addresses_ibfk_3', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['created_by'], ['id'])
        batch_op.drop_column('user_id')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_type', sa.String(length=150), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('user_type')

    with op.batch_alter_table('addresses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('addresses_ibfk_3', 'users', ['user_id'], ['id'])
        batch_op.drop_column('created_by')

    # ### end Alembic commands ###
