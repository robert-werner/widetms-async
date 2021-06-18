from fastapi import APIRouter, Query, HTTPException

from routers.tms_logic.router_logic import form_tasks

router = APIRouter()
"http://192.168.181.225:5000/tms_multi/T38WMS/12/2538/1072.tif@512?channels=(Sentinel-2,2020-06-03%2008:46:11,L1C,B11)"


@router.get('/tms/{alias}/{z}/{x}/{y}.tif@{res}')
async def tms(alias: str, z: int, x: int, y: int, res: int, channels: str = Query(None, regex=r"\(([^()]+)\)")):
    try:
        tasks = await form_tasks(alias, channels, z, x, y, res)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=400, detail={'type': str(e.__class__), 'text': str(e)})
