from fastapi_crudrouter import DatabasesCRUDRouter
from models.pydantic.aliases import Aliases, CreateAliases

from config.db import database
from models.aliases import t_aliases

alias_router = DatabasesCRUDRouter(
    schema=Aliases,
    create_schema=CreateAliases,
    table=t_aliases,
    database=database
)
