from sqlalchemy import Column, String, Table
from sqlalchemy.dialects.postgresql import UUID

from models.base import metadata

t_rs_devices = Table(
    'rs_devices', metadata,
    Column('id', UUID, primary_key=True),
    Column('rs_device', String(255), nullable=False),
    Column('description', String(1024))
)