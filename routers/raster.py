from typing import List, Optional

from fastapi import APIRouter

from models.raster import Raster

router = APIRouter()


@router.get("/raster", response_model=List[Raster])
async def get_rasters(alias: Optional[str] = None,
                      sensing_time: Optional[str] = None,
                      rs_device: Optional[str] = None,
                      spatial_res: Optional[int] = None,
                      unit: Optional[str] = None,
                      channel: Optional[str] = None,
                      processing_type: Optional[str] = None,
                      filepath: Optional[str] = None):
    query_args = {key: val for key, val in locals().items() if val is not None}
    fk_keys = dict(
        rs_device='info__rs_device_id__rs_device',
        spatial_res='info__spatial_res',
        unit='info__unit',
        channel='info__channel',
        processing_type='processing_type__processing_type'
    )
    fk_keys_in_qargs = query_args.keys() & fk_keys.keys()
    for _ in fk_keys_in_qargs:
        query_args[fk_keys[_]] = query_args.pop(_)
    return await Raster.objects.select_all().all(**query_args)
