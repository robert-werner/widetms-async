from config.celery_app import app as celery_app
from fastapi import APIRouter, Query, HTTPException

from routers.tms_logic.router_logic import form_tasks

router = APIRouter()


@router.get('/tms/{alias}/{z}/{x}/{y}.tif@{res}')
async def tms(alias: str, z: int, x: int, y: int, res: int, channels: str = Query(None, regex=r"\(([^()]+)\)")):
    try:
        bands = []
        tasks = await form_tasks(alias, channels, z, x, y, res)
        for task in tasks:
            bands.append(celery_app.send_task('widetms.worker.tile', (task,)))
        bands = [band.get() for band in bands]
        return len(bands)
    except Exception as e:
        raise HTTPException(status_code=400, detail={'type': str(e.__class__), 'text': str(e)})
