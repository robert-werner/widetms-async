from typing import List, Optional

from fastapi import APIRouter

from models.rs_device import RemoteSensingDevice

router = APIRouter()


@router.get("/rs_device", response_model=List[RemoteSensingDevice])
async def get_processing_types(rs_device: Optional[str] = None):
    query_args = {key: val for key, val in locals().items() if val is not None}
    return await RemoteSensingDevice.objects.all(**query_args)
