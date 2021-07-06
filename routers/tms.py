import gc
import os
import time
from tempfile import mkstemp
from typing import Optional

from fastapi import APIRouter, Query, HTTPException
from starlette.responses import FileResponse

from config.celery_app import app as celery_app
from routers.tms_logic.router_logic import form_tasks

router = APIRouter()


@router.get('/tms/{alias}/{z}/{x}/{y}.tif@{res}')
async def tms(alias: str, z: int, x: int, y: int, res: int, channels: str = Query(None, regex=r"\(([^()]+)\)"), resampling: Optional[str] = 'average', dtype: Optional[str] = 'float32'):
    tile_task = None
    final_tile = None
    temp_tile, path = mkstemp()
    start_time = time.time()
    try:
        bands = []
        tasks = await form_tasks(alias, channels, z, x, y, res, resampling, dtype)
        for task in tasks:
            band = celery_app.send_task('widetms.worker.tile', (task,))
            bands.append(band)
        tile_task = celery_app.send_task('widetms.builder.build', (bands, ))
        final_tile = tile_task.get()
        open(path, 'wb').write(final_tile)
        return FileResponse(path, filename=f"{y}.tiff")
    except Exception as e:
        raise HTTPException(status_code=400, detail={'type': str(e.__class__), 'text': str(e), 'execution_time': f"{time.time() - start_time} seconds"})
    finally:
        os.close(temp_tile)
        del tile_task, final_tile, temp_tile, path
        gc.collect()
