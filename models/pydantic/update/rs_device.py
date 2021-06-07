import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class CreateRsDevice(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    rs_device: str
    description: Optional[str]