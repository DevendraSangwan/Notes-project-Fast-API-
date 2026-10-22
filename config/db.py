import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError(
        "MONGO_URI is missing. Add your MongoDB connection string to the project .env file."
    )

conn = MongoClient(MONGO_URI)
