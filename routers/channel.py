from typing import List, Optional

from fastapi import APIRouter

from models.channel import Channel

router = APIRouter()


@router.get("/channel", response_model=List[Channel])
async def get_channels(spatial_res: Optional[int] = None,
                       unit: Optional[str] = None,
                       special: Optional[bool] = None,
                       rs_device: Optional[str] = None,
                       channel: Optional[str] = None,
                       recurse: Optional[str] = None):
    query_args = {key: val for key, val in locals().items() if val is not None}
    if 'rs_device' in query_args:
        query_args['rs_device_id__rs_device'] = query_args.pop('rs_device')
    if 'recurse' in query_args:
        del query_args['recurse']
    if recurse == '':
        return await Channel.objects.select_all().all(**query_args)
    return await Channel.objects.all(**query_args)
