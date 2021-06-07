import re
import uuid
from typing import List, Optional

from dateutil import parser
from fastapi import APIRouter, HTTPException
from fastapi_crudrouter import OrmarCRUDRouter

from models.alias import Alias
from models.channel import Channel
from models.pydantic.update.raster import CreateRaster
from models.raster import Raster
from models.processing_type import ProcessingType

router = OrmarCRUDRouter(
    schema=Raster,
    create_schema=Optional[CreateRaster]
)


@router.post('/l1c')
async def createl1c(filepath: str):
    try:
        result = []
        alias = re.findall(r'_(T\d+\w+)_', filepath)[0]
        db_alias = await Alias.objects.get_or_create(alias=alias, description=f"A Sentinel-2 '{alias}' MGRS tile")
        date_pieces = []
        for i in range(0, 6):
            date_pieces.append(
                re.findall(r"[CA]_(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})", filepath)[0][i])
        date = parser.parse('{}-{}-{} {}:{}:{}'.format(*date_pieces))
        db_l1c = await ProcessingType.objects.get(processing_type='L1C')
        for channel in ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12']:
            db_channel = await Channel.objects.get(channel=channel, rs_device_id__rs_device='Sentinel-2')
            db_raster = await Raster.objects.create(id=uuid.uuid4(), alias=db_alias, channel_id=db_channel, sensing_time=date,
                                                    processing_type=db_l1c, filepath=filepath.format(channel))
            result.append(db_raster)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
