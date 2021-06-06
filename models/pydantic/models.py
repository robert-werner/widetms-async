from uuid import UUID
import datetime
from typing import Optional
from pydantic import BaseModel


class Aliases(BaseModel):

    id: UUID
    alias: str
    description: Optional[str]


class ProcessingTypes(BaseModel):

    id: UUID
    processing_type: str
    description: Optional[str]


class RsDevices(BaseModel):

    id: UUID
    rs_device: str
    description: Optional[str]


class Channels(BaseModel):

    id: UUID
    channel: Optional[str]
    rs_device_id: UUID
    spatial_res: Optional[int]
    unit: Optional[str]
    description: Optional[str]
    special: bool
    formula: Optional[str]


class Rasters(BaseModel):

    id: UUID
    alias: UUID
    info: Optional[UUID]
    sensing_time: datetime.datetime
    processing_type: UUID
    filepath: str
