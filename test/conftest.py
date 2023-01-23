from fastapi.testclient import TestClient
from main import app
from geo.config import database
from motor.motor_asyncio import AsyncIOMotorClient

TEST_MONGO_URL = 'mongodb://db:27017/'
test_client = AsyncIOMotorClient(TEST_MONGO_URL)

override_database = test_client.test_db

app.dependency_overrides[database] = override_database

client = TestClient(app)
