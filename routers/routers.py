from typing import Optional

from fastapi_crudrouter import DatabasesCRUDRouter

from config import db
from config.db import database
from models.pydantic.models import Aliases, ProcessingTypes, RsDevices, Channels, Rasters
from models_nc import t_aliases, t_processing_types, t_rs_devices, t_channels, t_rasters

alias_router = DatabasesCRUDRouter(
    schema=Aliases,
    table=t_aliases,
    database=database
)

pt_router = DatabasesCRUDRouter(
    schema=ProcessingTypes,
    table=t_processing_types,
    database=database
)

rsd_router = DatabasesCRUDRouter(
    schema=RsDevices,
    table=t_rs_devices,
    database=database
)

channels_router = DatabasesCRUDRouter(
    schema=Channels,
    table=t_channels,
    database=database
)


@channels_router.get('')
async def overloaded_get_all():
    query = t_channels.join(t_rs_devices, left)
    return await database.fetch_all(query)


rasters_router = DatabasesCRUDRouter(
    schema=Rasters,
    table=t_rasters,
    database=database
)
