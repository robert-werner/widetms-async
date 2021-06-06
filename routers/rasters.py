import re

from fastapi_crudrouter import DatabasesCRUDRouter

from config.db import database
from models.pydantic.rasters import Rasters, CreateRasters
from models.rasters import t_rasters
from models.channels import t_channels
from models.aliases import t_aliases

rasters_router = DatabasesCRUDRouter(
    schema=Rasters,
    create_schema=CreateRasters,
    table=t_rasters,
    database=database
)


@rasters_router.post('/l1c')
async def create_l1c(filepath: str):
    alias = re.findall(r'_(T\d+\w+)_', filepath)[0]
    date_pieces = []
    for i in range(0, 6):
        date_pieces.append(
            re.findall(r"[CA]_(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})", filepath)[0][i])
    date = '{}-{}-{} {}:{}:{} UTC'.format(*date_pieces)
    pass
