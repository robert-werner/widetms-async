from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class RsDevices(BaseModel):
    id: UUID
    rs_device: str
    description: Optional[str]
