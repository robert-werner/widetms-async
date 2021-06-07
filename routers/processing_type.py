from typing import List, Optional

from fastapi import APIRouter
from fastapi_crudrouter import OrmarCRUDRouter

from models.processing_type import ProcessingType
from models.pydantic.update.processing_type import CreateProcessingType

router = OrmarCRUDRouter(
    schema=ProcessingType,
    create_schema=Optional[CreateProcessingType]
)