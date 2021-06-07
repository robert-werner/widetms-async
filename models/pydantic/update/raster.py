import datetime
import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class CreateRaster(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    alias: UUID
    channel_id: Optional[UUID]
    sensing_time: datetime.datetime
    processing_type: UUID
    filepath: str
