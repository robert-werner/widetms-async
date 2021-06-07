import re
from typing import Union, Tuple, List

from fastapi import APIRouter, Query, HTTPException

from models.alias import Alias
from models.processing_type import ProcessingType
from models.raster import Raster
from models.channel import Channel

router = APIRouter()
"http://192.168.181.225:5000/tms_multi/T38WMS/12/2538/1072.tif@512?channels=(Sentinel-2,2020-06-03%2008:46:11,L1C,B11)"


async def parse_channels(channels):
    bands = list()
    for i in list(range(len(re.findall(r"[^()]+", channels))))[::2]:
        band = re.findall(r"[^()]+", channels)[i].split(',')
        if len(band) < 4:
            raise SyntaxError(f"Insufficent band info at {str(i)} positional band {str(channels)}")
        bands.append(band)
    clean_params = [list(map(lambda param: param.strip(), param_list)) for param_list in bands]
    return clean_params


async def find_filepaths(db_alias, channels):
    filepaths = {'filepaths': []}
    for channel in channels:
        db_channel = await Channel.objects.get(channel=channel[3], rs_device_id__rs_device=channel[0])
        db_processing_type = await ProcessingType.objects.get(processing_type=channel[2])
        filepath = await Raster.objects.get(channel_id=db_channel.id, alias_id=db_alias.id, sensing_time=channel[1],
                                            processing_type_id=db_processing_type)
        filepaths['filepaths'].append(filepath.filepath)
    return filepaths


async def form_tasks(filepaths, db_alias, z, x, y, res):
    tasks = []
    for filepath in filepaths['filepaths']:
        task = {
            'filepath': filepath,
            'z': z,
            'x': x,
            'y': y,
            'resolution': res
        }
        tasks.append(task)
    return tasks


@router.get('/tms/{alias}/{z}/{x}/{y}.tif@{res}')
async def tms(alias: str, z: int, x: int, y: int, res: int, channels: str = Query(None, regex=r"\(([^()]+)\)")):
    try:
        db_alias = await Alias.objects.get(alias=alias)
        channels = await parse_channels(channels)
        filepaths = await find_filepaths(db_alias, channels)
        tasks = await form_tasks(filepaths, db_alias, z, x, y, res)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=400, detail={'type': str(e.__class__), 'text': str(e)})
