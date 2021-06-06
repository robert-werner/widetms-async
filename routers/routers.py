from fastapi_crudrouter import DatabasesCRUDRouter

from config.db import database
from models.aliases import t_aliases
from models.channels import t_channels
from models.processing_types import t_processing_types
from models.pydantic.models import Aliases, ProcessingTypes, RsDevices, Channels, Rasters
from models.rasters import t_rasters
from models.rs_devices import t_rs_devices

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

rasters_router = DatabasesCRUDRouter(
    schema=Rasters,
    table=t_rasters,
    database=database
)
