from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Aliases(BaseModel):

    id: UUID
    alias: str
    description: Optional[str]