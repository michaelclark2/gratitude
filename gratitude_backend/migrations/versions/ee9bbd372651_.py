"""empty message

Revision ID: ee9bbd372651
Revises: 
Create Date: 2019-12-12 17:29:19.058157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee9bbd372651'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gratitude',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('response', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_gratitude_user_id'), 'gratitude', ['user_id'], unique=False)
    op.create_table('prompt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firebase_id', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('firebase_id')
    )
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('prompt_id', sa.Integer(), nullable=True),
    sa.Column('response', sa.String(length=5000), nullable=True),
    sa.ForeignKeyConstraint(['prompt_id'], ['prompt.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entry_user_id'), 'entry', ['user_id'], unique=False)
    op.create_table('user_grats',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('grat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['grat_id'], ['gratitude.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('prompt_entries',
    sa.Column('entry_id', sa.Integer(), nullable=True),
    sa.Column('prompt_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['entry_id'], ['entry.id'], ),
    sa.ForeignKeyConstraint(['prompt_id'], ['prompt.id'], )
    )
    op.create_table('user_entries',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('entry_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['entry_id'], ['entry.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_entries')
    op.drop_table('prompt_entries')
    op.drop_table('user_grats')
    op.drop_index(op.f('ix_entry_user_id'), table_name='entry')
    op.drop_table('entry')
    op.drop_table('user')
    op.drop_table('prompt')
    op.drop_index(op.f('ix_gratitude_user_id'), table_name='gratitude')
    op.drop_table('gratitude')
    # ### end Alembic commands ###
