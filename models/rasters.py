from sqlalchemy import Column, String, Table, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

from models.base import metadata

t_rasters = Table(
    'rasters', metadata,
    Column('id', UUID, primary_key=True),
    Column('alias', ForeignKey('aliases.id'), nullable=False, index=True),
    Column('info', ForeignKey('channels.id'), index=True),
    Column('sensing_time', DateTime, nullable=False),
    Column('processing_type', ForeignKey('processing_types.id'), nullable=False, index=True),
    Column('filepath', String(255), nullable=False)
)