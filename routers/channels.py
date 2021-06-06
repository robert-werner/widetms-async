from fastapi_crudrouter import DatabasesCRUDRouter

from config.db import database
from models.channels import t_channels
from models.pydantic.channels import Channels, CreateChannels

channels_router = DatabasesCRUDRouter(
    schema=Channels,
    create_schema=CreateChannels,
    table=t_channels,
    database=database
)