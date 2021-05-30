import uuid
from typing import Optional, Literal

import ormar
from ormar import property_field

from models.base import BaseMeta
from models.rs_device import RemoteSensingDevice


class Channel(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'channels'

    id: uuid.UUID = ormar.UUID(primary_key=True)
    channel: str = ormar.String(max_length=255)
    rs_device_id: Optional[RemoteSensingDevice] = ormar.ForeignKey(RemoteSensingDevice, skip_reverse=False)
    spatial_res: int = ormar.Integer(nullable=True)
    unit: str = ormar.String(max_length=255, nullable=True)
    description: str = ormar.String(max_length=1024)
    special: bool = ormar.Boolean(nullable=False)
    formula: str = ormar.Text()