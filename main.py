import uvicorn
from fastapi import FastAPI

from config.db import database
from routers.routers import alias_router, pt_router, rsd_router, channels_router, rasters_router

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
    uvicorn.run(app, host="0.0.0.0", port=8000)
