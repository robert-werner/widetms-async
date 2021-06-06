import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class RsDevices(BaseModel):
    id: UUID
    rs_device: str
    description: Optional[str]


class CreateRsDevices(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    rs_device: str
    description: Optional[str]
