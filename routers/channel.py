from typing import Optional

from fastapi_crudrouter import OrmarCRUDRouter

from models.channel import Channel
from models.pydantic.update.channel import CreateChannel

router = OrmarCRUDRouter(
    schema=Channel,
    create_schema=Optional[CreateChannel]
)