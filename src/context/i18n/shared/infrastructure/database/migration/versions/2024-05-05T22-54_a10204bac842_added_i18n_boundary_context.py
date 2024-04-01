"""Added i18n boundary context

Revision ID: a10204bac842
Revises: 
Create Date: 2024-05-05 22:54:47.023289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a10204bac842'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('script',
    sa.Column('comment', sa.ARRAY(sa.VARCHAR(length=1)), nullable=False),
    sa.Column('subtag', sa.CHAR(length=4), nullable=False),
    sa.Column('description', sa.ARRAY(sa.VARCHAR(length=1)), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('subtag')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('script')
    # ### end Alembic commands ###
