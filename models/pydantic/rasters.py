import datetime
import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, validator


class Rasters(BaseModel):
    id: UUID
    alias: UUID
    channel_id: Optional[UUID]
    sensing_time: datetime.datetime
    processing_type: UUID
    filepath: str


class CreateRasters(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    alias: UUID
    channel_id: Optional[UUID]
    sensing_time: datetime.datetime
    processing_type: UUID
    filepath: str
