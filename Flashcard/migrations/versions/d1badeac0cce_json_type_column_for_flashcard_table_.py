"""Json type column for Flashcard table problem debug 3

Revision ID: d1badeac0cce
Revises: 
Create Date: 2025-03-04 23:57:29.324084

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd1badeac0cce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Flashcard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pack_id', sa.Integer(), nullable=True),
    sa.Column('Key', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('value', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Flashcard', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Flashcard_Key'), ['Key'], unique=False)
        batch_op.create_index(batch_op.f('ix_Flashcard_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_Flashcard_pack_id'), ['pack_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_Flashcard_value'), ['value'], unique=False)

    op.create_table('Flashcard_pack',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Flashcard_pack', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Flashcard_pack_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_Flashcard_pack_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_Flashcard_pack_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Flashcard_pack', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Flashcard_pack_name'))
        batch_op.drop_index(batch_op.f('ix_Flashcard_pack_description'))
        batch_op.drop_index(batch_op.f('ix_Flashcard_pack_created_at'))

    op.drop_table('Flashcard_pack')
    with op.batch_alter_table('Flashcard', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Flashcard_value'))
        batch_op.drop_index(batch_op.f('ix_Flashcard_pack_id'))
        batch_op.drop_index(batch_op.f('ix_Flashcard_created_at'))
        batch_op.drop_index(batch_op.f('ix_Flashcard_Key'))

    op.drop_table('Flashcard')
    # ### end Alembic commands ###
