import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class CreateProcessingType(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    processing_type: str
    description: Optional[str]