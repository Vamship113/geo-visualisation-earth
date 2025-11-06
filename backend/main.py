from backend.db.mongodb import connect_to_mongo,close_mongo_connection
from fastapi import FastAPI
from contextlib import asynccontextmanager 
from backend.routes.sunrise_sunset_routes import router as sunrise_sunset_router
from backend.routes.weather import router as weather_router
from backend.routes.air_quality_routes import router as air_quality_router
@asynccontextmanager
async def db_lifespan(app: FastAPI):
    await connect_to_mongo()
    yield

    await close_mongo_connection()

app=FastAPI(title="Geo Visualizer Backend",lifespan=db_lifespan)
app.include_router(sunrise_sunset_router,prefix="/api")
app.include_router(weather_router,prefix="/api")
app.include_router(air_quality_router,prefix="/api")

@app.get("/")
def home():
    return {"status":"ok", "message":"backend running"}
