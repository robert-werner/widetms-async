import datetime
import os
import uuid
from typing import Optional

import ormar

from models.alias import Alias
from models.base import BaseMeta
from models.channel import Channel
from models.processing_type import ProcessingType


class RastersJoined(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'rasters_joined'

    id: uuid.UUID = ormar.UUID(primary_key=True, default=uuid.uuid4())
    alias: Optional[Alias] = ormar.String(nullable=False, max_length=255)
    channel_id: Optional[Channel] = ormar.ForeignKey(Channel, skip_reverse=True)
    sensing_time: datetime.datetime = ormar.DateTime(nullable=False)
    processing_type_id: Optional[ProcessingType] = ormar.ForeignKey(ProcessingType, skip_reverse=True)
    filepath: os.PathLike = ormar.String(nullable=False, max_length=255)
