from typing import Optional

from fastapi_crudrouter import OrmarCRUDRouter

from models.alias import Alias
from models.pydantic.update.alias import CreateAlias

router = OrmarCRUDRouter(
    schema=Alias,
    create_schema=Optional[CreateAlias]
)