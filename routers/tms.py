import gc
import os
import time
from typing import Optional

from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse
from starlette.background import BackgroundTasks

from config.celery_app import app as celery_app
from routers.tms_logic.builder import build
from routers.tms_logic.router_logic import form_tasks

router = APIRouter()


def remove_file(path: str) -> None:
    try:
        if os.path.exists(path):
            os.unlink(path)
    except FileNotFoundError:
        pass


@router.get('/tms/{alias}/{z}/{x}/{y}.tif@{res}')
async def tms(background_tasks: BackgroundTasks, alias: str, z: int, x: int, y: int, res: int,
              channels: str = Query(None, regex=r"\(([^()]+)\)"),
              resampling: Optional[str] = 'average', dtype: Optional[str] = 'float32'):
    start_time = time.time()
    bands = []
    try:
        tasks = await form_tasks(alias, channels, z, x, y, res, resampling, dtype)
        for task in tasks:
            band = celery_app.send_task('widetms.worker.tile', (task,))
            bands.append(band)
        final_tile = build(bands)
        background_tasks.add_task(remove_file, final_tile)
        return FileResponse(final_tile, filename=f"{y}.tiff")
    except Exception as e:
        raise HTTPException(status_code=400, detail={'type': str(e.__class__), 'text': str(e),
                                                     'execution_time': f"{time.time() - start_time} seconds"})
    finally:
        del bands
        gc.collect()
