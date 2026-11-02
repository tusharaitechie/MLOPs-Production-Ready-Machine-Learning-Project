import os
import ssl
import certifi
from pymongo import MongoClient

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

client = MongoClient(
    MONGO_DB_URL,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=15000
)

try:
    print(client.admin.command("ping"))
    print("MongoDB Connected Successfully!")

except Exception as e:
    print(type(e).__name__)
    print(e)

finally:
    client.close()