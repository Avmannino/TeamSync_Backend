"""empty message

Revision ID: 1ac867b6fad4
Revises: 
Create Date: 2024-04-16 10:42:08.525375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ac867b6fad4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitcher_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('wins', sa.Integer(), nullable=True),
    sa.Column('losses', sa.Integer(), nullable=True),
    sa.Column('era', sa.Float(), nullable=True),
    sa.Column('games_started', sa.Integer(), nullable=True),
    sa.Column('innings_pitched', sa.Float(), nullable=True),
    sa.Column('strikeouts', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_pitcher_table'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitcher_table')
    # ### end Alembic commands ###