"""create boasts table

Revision ID: 1e107593f4ce
Revises: None
Create Date: 2013-09-19 21:28:08.456063

"""

# revision identifiers, used by Alembic.
revision = '1e107593f4ce'
down_revision = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'boasts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('boasts')

