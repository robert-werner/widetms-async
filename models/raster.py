import datetime
import os
import uuid
from typing import Optional

import ormar

from models.base import BaseMeta
from models.rs_device import RemoteSensingDevice
from models.processing_type import ProcessingType
from models.alias import Alias
from models.channel import Channel


class Raster(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'rasters'

    id: uuid.UUID = ormar.UUID(primary_key=True)
    alias: Optional[Alias] = ormar.ForeignKey(Alias, skip_reverse=True)
    info: Optional[Channel] = ormar.ForeignKey(Channel, skip_reverse=True)
    sensing_time: datetime.datetime = ormar.DateTime(nullable=False)
    processing_type: Optional[ProcessingType] = ormar.ForeignKey(ProcessingType, skip_reverse=True)
    filepath: os.PathLike = ormar.String(nullable=False, max_length=255)
