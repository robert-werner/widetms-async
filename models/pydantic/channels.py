import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Channels(BaseModel):
    id: UUID
    channel: Optional[str]
    rs_device_id: UUID
    spatial_res: Optional[int]
    unit: Optional[str]
    description: Optional[str]
    special: bool
    formula: Optional[str]


class CreateChannels(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    channel: Optional[str]
    rs_device_id: UUID
    spatial_res: Optional[int]
    unit: Optional[str]
    description: Optional[str]
    special: bool
    formula: Optional[str]
