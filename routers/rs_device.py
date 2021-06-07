from typing import Optional

from fastapi_crudrouter import OrmarCRUDRouter

from models.pydantic.update.rs_device import CreateRsDevice
from models.rs_device import RemoteSensingDevice

router = OrmarCRUDRouter(
    schema=RemoteSensingDevice,
    create_schema=Optional[CreateRsDevice]
)
