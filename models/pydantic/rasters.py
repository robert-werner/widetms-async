from uuid import UUID
import datetime
from typing import Optional
from pydantic import BaseModel


class Rasters(BaseModel):
    id: UUID
    alias: UUID
    info: Optional[UUID]
    sensing_time: datetime.datetime
    processing_type: UUID
    filepath: str
