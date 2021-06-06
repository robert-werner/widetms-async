from fastapi_crudrouter import DatabasesCRUDRouter

from config.db import database
from models.pydantic.rs_devices import RsDevices, CreateRsDevices
from models.rs_devices import t_rs_devices

rsd_router = DatabasesCRUDRouter(
    schema=RsDevices,
    create_schema=CreateRsDevices,
    table=t_rs_devices,
    database=database
)