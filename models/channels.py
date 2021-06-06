import uuid

from sqlalchemy import Column, String, Table, ForeignKey, Integer, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID

from models.base import metadata


t_channels = Table(
    'channels', metadata,
    Column('id', UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False),
    Column('channel', String(255)),
    Column('rs_device_id', ForeignKey('rs_devices.id'), nullable=False, index=True),
    Column('spatial_res', Integer),
    Column('unit', String(255)),
    Column('description', String(1024)),
    Column('special', Boolean, nullable=False),
    Column('formula', Text)
)