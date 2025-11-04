from pymongo import MongoClient

import os
from dotenv import load_dotenv
from pymongo import AsyncMongoClient
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME= os.getenv("MONGO_DB_NAME")
client = None
db=None

async def connect_to_mongo():
    global client, db
    try:
        client=AsyncMongoClient(MONGO_URI)
        db=client[MONGO_DB_NAME]
        print("Mongodb connected successful")
    except Exception as e:
        print("Mongodb failed to connect")


async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("MongoDB connection closed ")