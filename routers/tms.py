import tempfile
from io import BytesIO

from starlette.responses import FileResponse

from config.celery_app import app as celery_app
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import StreamingResponse
from routers.tms_logic.router_logic import form_tasks
import time

router = APIRouter()


@router.get('/tms/{alias}/{z}/{x}/{y}.tif@{res}')
async def tms(alias: str, z: int, x: int, y: int, res: int, channels: str = Query(None, regex=r"\(([^()]+)\)")):
    start_time = time.time()
    try:
        bands = []
        tasks = await form_tasks(alias, channels, z, x, y, res)
        for task in tasks:
            band = celery_app.send_task('widetms.worker.tile', (task,))
            bands.append(band)
        tile = celery_app.send_task('widetms.builder.build', (bands, ))
        open(f"{y}.tiff", 'wb').write(tile.get())
        return FileResponse(f"{y}.tiff", filename=f"{y}.tiff")
    except Exception as e:
        raise HTTPException(status_code=400, detail={'type': str(e.__class__), 'text': str(e), 'execution_time': f"{time.time() - start_time} seconds"})
