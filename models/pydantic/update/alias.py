import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class CreateAlias(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    alias: str
    description: Optional[str]