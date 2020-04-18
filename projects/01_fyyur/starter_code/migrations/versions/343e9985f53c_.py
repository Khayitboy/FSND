"""empty message

Revision ID: 343e9985f53c
Revises: d861eabbdb82
Create Date: 2020-04-16 14:26:11.329854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '343e9985f53c'
down_revision = 'd861eabbdb82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('venue_artists')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venue_artists',
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='venue_artists_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='venue_artists_venue_id_fkey'),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id', name='venue_artists_pkey')
    )
    op.drop_table('show')
    # ### end Alembic commands ###
