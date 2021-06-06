import uuid

from sqlalchemy import Column, String, Table
from sqlalchemy.dialects.postgresql import UUID

from models.base import metadata

t_processing_types = Table(
    'processing_types', metadata,
    Column('id', UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False),
    Column('processing_type', String(255), nullable=False),
    Column('description', String(1024))
)