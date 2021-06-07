import uuid

import ormar

from models.base import BaseMeta

class RemoteSensingDevice(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'rs_devices'

    id: uuid.UUID = ormar.UUID(primary_key=True, default=uuid.uuid4())
    rs_device: str = ormar.String(max_length=255, nullable=False)
    description: str = ormar.String(max_length=1024, nullable=True)