from fastapi_crudrouter import DatabasesCRUDRouter

from config.db import database
from models.processing_types import t_processing_types
from models.pydantic.processing_types import ProcessingTypes, CreateProcessingTypes

pt_router = DatabasesCRUDRouter(
    schema=ProcessingTypes,
    create_schema=CreateProcessingTypes,
    table=t_processing_types,
    database=database
)
