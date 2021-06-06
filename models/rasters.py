import uuid

from sqlalchemy import Column, String, Table, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

from models.base import metadata

t_rasters = Table(
    'rasters', metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()),
    Column('alias', ForeignKey('aliases.id'), nullable=False, index=True),
    Column('channel_id', ForeignKey('channels.id'), index=True),
    Column('sensing_time', DateTime, nullable=False),
    Column('processing_type', ForeignKey('processing_types.id'), nullable=False, index=True),
    Column('filepath', String(255), nullable=False)
)