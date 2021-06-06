from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Channels(BaseModel):
    id: UUID
    channel: Optional[str]
    rs_device_id: UUID
    spatial_res: Optional[int]
    unit: Optional[str]
    description: Optional[str]
    special: bool
    formula: Optional[str]
