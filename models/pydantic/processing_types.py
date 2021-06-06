from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ProcessingTypes(BaseModel):
    id: UUID
    processing_type: str
    description: Optional[str]
