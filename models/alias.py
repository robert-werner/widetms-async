import uuid

import ormar

from models.base import BaseMeta


class Alias(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'aliases'

    id: uuid.UUID = ormar.UUID(primary_key=type, default=uuid.uuid4())
    alias: str = ormar.String(max_length=255)
    description: str = ormar.String(max_length=1024)
