import uvicorn

import config.db
from app import app
from routers.channel import router as channel_router
from routers.processing_type import router as pt_router
from routers.rs_device import router as rsd_router
from routers.alias import router as alias_router
from routers.raster import router as raster_router


@app.on_event("startup")
async def startup() -> None:
    database_ = config.db.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = config.db.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(channel_router)
app.include_router(pt_router)
app.include_router(rsd_router)
app.include_router(alias_router)
app.include_router(raster_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
