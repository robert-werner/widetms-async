import uuid

import ormar

from models.base import BaseMeta


class ProcessingType(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'processing_types'

    id: uuid.UUID = ormar.UUID(primary_key=type)
    processing_type: str = ormar.String(max_length=255)
    description: str = ormar.String(max_length=1024)