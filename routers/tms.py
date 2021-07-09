import gc
import os
import time
from typing import Optional

from fastapi import APIRouter, Query, HTTPException
from starlette.responses import FileResponse

from config.celery_app import app as celery_app
from routers.tms_logic.router_logic import form_tasks

router = APIRouter()


@router.get('/tms/{alias}/{z}/{x}/{y}.tif@{res}')
async def tms(alias: str, z: int, x: int, y: int, res: int, channels: str = Query(None, regex=r"\(([^()]+)\)"), resampling: Optional[str] = 'average', dtype: Optional[str] = 'float32'):
    start_time = time.time()
    try:
        bands = []
        tasks = await form_tasks(alias, channels, z, x, y, res, resampling, dtype)
        for task in tasks:
            band = celery_app.send_task('widetms.worker.tile', (task,))
            bands.append(band)
        tile_task = celery_app.send_task('widetms.builder.build', (bands, ))
        final_tile = tile_task.get()
        open(f"{y}.tiff", 'wb').write(final_tile)
        return FileResponse(f"{y}.tiff", filename=f"{y}.tiff")
    except Exception as e:
        raise HTTPException(status_code=400, detail={'type': str(e.__class__), 'text': str(e), 'execution_time': f"{time.time() - start_time} seconds"})
    finally:
        gc.collect()
