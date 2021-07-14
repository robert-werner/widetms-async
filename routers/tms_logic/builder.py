import uuid

import rasterio


def build(divided_bands):
    bands = [band.get() for band in divided_bands]
    filename = f"{str(uuid.uuid4())[0:6]}.tiff"
    try:
        band_count = len(bands)
        with rasterio.Env(GDAL_NUM_THREADS='ALL_CPUs'):
            with rasterio.open(filename, 'w', driver='GTiff',
                               height=bands[0].shape[0],
                               width=bands[0].shape[1],
                               count=band_count,
                               dtype=bands[0].dtype) as dst:
                for id, band in enumerate(bands, 1):
                    dst.write_band(id, band)
        return filename
    except Exception as e:
        raise Exception(str(e))
    finally:
        [band.forget() for band in divided_bands]
