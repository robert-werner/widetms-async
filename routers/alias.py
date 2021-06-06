from fastapi_crudrouter import DatabasesCRUDRouter
from models.pydantic.aliases import Aliases

from config.db import database
from models.aliases import t_aliases

alias_router = DatabasesCRUDRouter(
    schema=Aliases,
    table=t_aliases,
    database=database
)
