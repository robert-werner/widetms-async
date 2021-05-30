from typing import List, Optional

from fastapi import APIRouter

from models.alias import Alias

router = APIRouter()


@router.get("/alias", response_model=List[Alias])
async def get_aliases(alias: Optional[str] = None):
    query_args = {key: val for key, val in locals().items() if val is not None}
    return await Alias.objects.all(**query_args)
