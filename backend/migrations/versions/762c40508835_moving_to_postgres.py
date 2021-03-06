"""moving to postgres

Revision ID: 762c40508835
Revises: c60335b70c1c
Create Date: 2020-06-01 08:55:55.054048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '762c40508835'
down_revision = 'c60335b70c1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('view_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip_address', sa.String(length=32), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_view_history_created'), 'view_history', ['created'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_view_history_created'), table_name='view_history')
    op.drop_table('view_history')
    # ### end Alembic commands ###
