from db.mongodb import connect_to_mongo,close_mongo_connection
from fastapi import FastAPI
from contextlib import asynccontextmanager 
app=FastAPI()

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    await connect_to_mongo()
    yield

    await close_mongo_connection()


app: FastAPI = FastAPI(lifespan=db_lifespan)

@app.get("/")
def home():
    return {"status":"ok", "message":"backend running"}