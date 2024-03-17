"""Init1

Revision ID: 40689cc3896b
Revises: f354b90070f5
Create Date: 2024-03-17 15:06:46.447853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40689cc3896b'
down_revision: Union[str, None] = 'f354b90070f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grades', sa.Column('date_received', sa.DateTime(), nullable=True))
    op.drop_column('grades', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grades', sa.Column('date', sa.DATE(), nullable=True))
    op.drop_column('grades', 'date_received')
    # ### end Alembic commands ###