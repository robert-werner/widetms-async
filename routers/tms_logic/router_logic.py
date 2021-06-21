import re
from aiocache import cached
from aiocache.serializers import JsonSerializer
from models.alias import Alias
from models.channel import Channel
from models.processing_type import ProcessingType
from models.raster import Raster
from config.celery_app import app


@cached(serializer=JsonSerializer())
async def parse_channels(channels):
    bands = list()
    for i in list(range(len(re.findall(r"[^()]+", channels))))[::2]:
        band = re.findall(r"[^()]+", channels)[i].split(',')
        if len(band) < 4:
            raise SyntaxError(f"Insufficent band info at {str(i)} positional band {str(channels)}")
        bands.append(band)
    clean_params = [list(map(lambda param: param.strip(), param_list)) for param_list in bands]
    return clean_params


@cached(serializer=JsonSerializer())
async def find_filepaths(db_alias, channels):
    filepaths = {'filepaths': []}
    for channel in channels:
        db_channel = await Channel.objects.get(channel=channel[3], rs_device_id__rs_device=channel[0])
        db_processing_type = await ProcessingType.objects.get(processing_type=channel[2])
        filepath = await Raster.objects.get(channel_id=db_channel.id, alias_id=db_alias.id, sensing_time=channel[1],
                                            processing_type_id=db_processing_type)
        filepaths['filepaths'].append(filepath.filepath)
    return filepaths


@cached(serializer=JsonSerializer())
async def form_tasks(alias, channels, z, x, y, res):
    db_alias = await Alias.objects.get(alias=alias)
    channels = await parse_channels(channels)
    filepaths = await find_filepaths(db_alias, channels)
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
