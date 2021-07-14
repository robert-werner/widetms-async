import re

import ormar.exceptions
from aiocache import cached
from aiocache.serializers import JsonSerializer
from models.alias import Alias
from models.channel import Channel
from models.processing_type import ProcessingType
from models.raster import Raster
from models.rs_device import RemoteSensingDevice


async def find_alias(alias):
    try:
        return await Alias.objects.get(alias=alias)
    except ormar.exceptions.NoMatch:
        raise Exception(f"There is no alias by name {alias}")


async def find_rs_device(rs_device):
    try:
        return await RemoteSensingDevice.objects.get(rs_device=rs_device)
    except ormar.exceptions.NoMatch:
        raise Exception(f"There is no remote sensing device by name {rs_device}")


async def find_channel(channel, rs_device):
    try:
        return await Channel.objects.get(channel=channel, rs_device_id__rs_device=rs_device)
    except ormar.exceptions.NoMatch:
        raise Exception(f"There is no {channel} channel for remote sensing device {rs_device}")


async def find_processing_type(processing_type):
    try:
        return await ProcessingType.objects.get(processing_type=processing_type)
    except ormar.exceptions.NoMatch:
        raise Exception(f"There is no {processing_type} processing type")


async def find_raster_channel(channel, alias, processing_type, date=None):
    try:
        if not date:
            return await Raster.objects.get(channel_id=channel.id,
                                            alias_id=alias.id,
                                            processing_type_id=processing_type.id)
        else:
            return await Raster.objects.get(channel_id=channel.id,
                                            alias_id=alias.id,
                                            sensing_time=date,
                                            processing_type_id=processing_type.id)
    except ormar.exceptions.NoMatch:
        if date:
            raise Exception(
                f"There is no filepath corresponding to {date} sensing time and params: {channel.channel}, {alias.alias}, {processing_type.processing_type} (consider adding georaster)")
        else:
            raise Exception(
                f"There is no filepath corresponding to params: {channel.channel}, {alias.alias}, {processing_type.processing_type} (consider adding georaster)")


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
async def parametrize_bands(alias, channels):
    band_param = {'filepaths': [],
                  'bands': [],
                  'expressions': [],
                  'dtype': [],
                  'resampling': [],
                  'rs_device': []}
    db_alias = await find_alias(alias)
    for channel in channels:
        await find_rs_device(channel[0])
        db_channel = await find_channel(channel[3], channel[0])
        _channels = []
        _bands = []
        if db_channel.special:
            channels_special = list(set(re.findall(r"(?P<bands>[VH]{1,2}|B[0-9A]{1,2})", db_channel.formula)))
            for _channel in channels_special:
                db_processing_type = await find_processing_type(channel[2])
                _db_channel = await find_channel(_channel, channel[0])
                await find_raster_channel(_db_channel,
                                          db_alias,
                                          db_processing_type)
                filepath = await find_raster_channel(_db_channel,
                                                     db_alias,
                                                     db_processing_type,
                                                     channel[1])
                _channels.append(filepath.filepath)
                _bands.append(_channel)
        else:
            db_processing_type = await find_processing_type(channel[2])
            await find_raster_channel(db_channel,
                                      db_alias,
                                      db_processing_type)
            filepath = await find_raster_channel(db_channel,
                                                 db_alias,
                                                 db_processing_type,
                                                 channel[1])
            _channels.append(filepath.filepath)
            _bands.append(channel[3])
        channel_formula = None
        if db_channel.formula is not None:
            channel_formula = db_channel.formula
        band_param['filepaths'].append(_channels)
        band_param['bands'].append(_bands)
        band_param['expressions'].append(channel_formula)
        band_param['dtype'].append(channel[4])
        band_param['resampling'].append(channel[5])
        band_param['rs_device'].append(channel[0])
    return band_param

@cached(serializer=JsonSerializer())
async def form_tasks(alias, channels, z, x, y, res, resampling='average', dtype='float32'):
    channels = await parse_channels(channels, resampling, dtype)
    filepaths = await parametrize_bands(alias, channels)
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
        tasks.append(task)
    return tasks
