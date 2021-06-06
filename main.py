import uvicorn
from fastapi import FastAPI

from config.db import database
from routers.alias import alias_router
from routers.processing_types import pt_router
from routers.rs_devices import rsd_router
from routers.channels import channels_router
from routers.rasters import rasters_router

app = FastAPI()

app.include_router(alias_router)
app.include_router(pt_router)
app.include_router(rsd_router)
app.include_router(channels_router)
app.include_router(rasters_router)




@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
