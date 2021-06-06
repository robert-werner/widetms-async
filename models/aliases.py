import uuid

from sqlalchemy import Column, String, Table
from sqlalchemy.dialects.postgresql import UUID

from models.base import metadata

t_aliases = Table(
    'aliases', metadata,
    Column('id', UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False),
    Column('alias', String(255), nullable=False),
    Column('description', String(1024))
)