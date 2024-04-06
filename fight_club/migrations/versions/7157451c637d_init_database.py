"""init_database

Revision ID: 7157451c637d
Revises: 
Create Date: 2024-04-03 15:21:53.878982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7157451c637d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fighter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('fight_art', sa.Enum('UFC', 'Karate', native_enum=False), nullable=False),
    sa.Column('fights', sa.Integer(), nullable=False),
    sa.Column('wins', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='fight_club'
    )
    op.create_index(op.f('ix_fight_club_fighter_name'), 'fighter', ['name'], unique=True, schema='fight_club')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fight_club_fighter_name'), table_name='fighter', schema='fight_club')
    op.drop_table('fighter', schema='fight_club')
    # ### end Alembic commands ###
