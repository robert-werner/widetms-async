import re
from aiocache import cached
from aiocache.serializers import JsonSerializer

from models.alias import Alias
from models.channel import Channel
from models.processing_type import ProcessingType
from models.raster import Raster


@cached(serializer=JsonSerializer())
async def parse_channels(channels, resampling, dtype):
    bands = list()
    for i in list(range(len(re.findall(r"[^()]+", channels))))[::2]:
        band = re.findall(r"[^()]+", channels)[i].split(',')
        if len(band) < 4:
            raise SyntaxError(f"Insufficent band info at {str(i)} positional band {str(channels)}")
        band.append(dtype)
        band.append(resampling)
        bands.append(band)
    clean_params = [list(map(lambda param: param.strip(), param_list)) for param_list in bands]
    return clean_params


@cached(serializer=JsonSerializer())
async def parametrize_bands(db_alias, channels):
    print(channels)
    band_param = {'filepaths': [],
                  'bands': [],
                  'expressions': [],
                  'dtype': [],
                  'resampling': [],
                  'rs_device': []}
    for channel in channels:
        db_channel = await Channel.objects.get(channel=channel[3], rs_device_id__rs_device=channel[0])
        _channels = []
        _bands = []
        if db_channel.special:
            channels_special = list(set(re.findall(r"(?P<bands>[VH]{1,2}|B[0-9A]{1,2})", db_channel.formula)))
            for _channel in channels_special:
                db_processing_type = await ProcessingType.objects.get(processing_type=channel[2])
                _db_channel = await Channel.objects.get(channel=_channel, rs_device_id__rs_device=channel[0])
                filepath = await Raster.objects.get(channel_id=_db_channel.id, alias_id=db_alias.id,
                                                    sensing_time=channel[1],
                                                    processing_type_id=db_processing_type)
                _channels.append(filepath.filepath)
                _bands.append(_channel)
            band_param['filepaths'].append(_channels)
            band_param['bands'].append(_bands)
            band_param['expressions'].append(db_channel.formula)
            band_param['dtype'].append(channel[4])
            band_param['resampling'].append(channel[5])
            band_param['rs_device'].append(channel[0])
        else:
            db_processing_type = await ProcessingType.objects.get(processing_type=channel[2])
            filepath = await Raster.objects.get(channel_id=db_channel.id, alias_id=db_alias.id, sensing_time=channel[1],
                                                processing_type_id=db_processing_type)
            _channels.append(filepath.filepath)
            _bands.append(channel[3])
            band_param['filepaths'].append(_channels)
            band_param['bands'].append(_bands)
            band_param['expressions'].append(None)
            band_param['dtype'].append(channel[4])
            band_param['resampling'].append(channel[5])
            band_param['rs_device'].append(channel[0])
    return band_param


@cached(serializer=JsonSerializer())
async def form_tasks(alias, channels, z, x, y, res, resampling='average', dtype='float32'):
    db_alias = await Alias.objects.get(alias=alias)
    channels = await parse_channels(channels, resampling, dtype)
    filepaths = await parametrize_bands(db_alias, channels)
    tasks = []
    for filepath in zip(filepaths['filepaths'], filepaths['bands'], filepaths['expressions'], filepaths['dtype'],
                        filepaths['resampling'], filepaths['rs_device']):
        task = {
            'filepaths': filepath[0],
            'bands': filepath[1],
            'expressions': filepath[2],
            'z': z,
            'x': x,
            'y': y,
            'resolution': res,
            'dtype': filepath[3],
            'resampling': filepath[4],
            'rs_device': filepath[5]
        }
        print(task)
        tasks.append(task)
    return tasks
