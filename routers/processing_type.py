from typing import List, Optional

from fastapi import APIRouter

from models.processing_type import ProcessingType

router = APIRouter()

@router.get("/processing_type", response_model=List[ProcessingType])
async def get_processing_types(processing_type: Optional[str] = None):
    query_args = {key: val for key, val in locals().items() if val is not None}
    return await ProcessingType.objects.all(**query_args)
