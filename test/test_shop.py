import json
import pytest
from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from starlette import status
from geo.repository import ShopRepo
from geo.model import Shop
from main import app


TEST_MONGO_URL = 'mongodb://localhost:27017'
test_client = AsyncIOMotorClient(TEST_MONGO_URL)
override_database = test_client.test_db

client = TestClient(app)

@pytest.fixture
def shop_data():
    data = {
        "name": "test_name",
        "latitude": 0,
        "longitude": 0,
        "address": "string",
        "city": "string"
    }
    return data

    
@pytest.mark.asyncio
async def test_create_shop(shop_data):
    response = client.post("/shop/create/", json=shop_data)
    assert response.status_code == 201
    assert response.json()["status"] == "Ok"
    assert response.json()["message"] == "Success save data"


@pytest.mark.asyncio
async def test_get_shops():
    shop_data = {
        "name": "test_name",
        "latitude": 0,
        "longitude": 0,
        "address": "string",
        "city": "string"
    }
    await ShopRepo.insert(Shop(**shop_data))
    response = await client.get("/shop/")
    json_response = json.loads(response.content)
    assert json_response["code"] == 200
    assert json_response["status"] == "Ok"
    assert json_response["message"] == "Success retrieve all data"
    assert json_response["result"]
    assert json_response["result"][0]["name"] == shop_data["name"]



@pytest.mark.asyncio
async def test_get_particular_shop(shop_id):
    response = await client.get(f"/shop/{shop_id}")
    assert response.status_code == 200
    json_response = json.loads(response.content)
    assert json_response['code'] == 200
    assert json_response['status'] == 'Ok'
    assert json_response['message'] == 'Success retrieve data'
  

@pytest.mark.asyncio
async def test_update_shop(shop_data):
    shop = await test_create_shop(shop_data)
    shop_id = str(shop['_id']['$oid'])
    updated_data = {
        "name": "updated_name",
    }
    response = await client.put(f"/shop/{shop_id}/", json=updated_data)
    assert response.status_code == 200
    json_response = json.loads(response.content)
    assert json_response['status'] == 'Ok'
    assert json_response['message'] == 'Success update data'


@pytest.mark.asyncio
async def test_delete_shop():
    shop_data = {
        "name": "test_name",
        "latitude": 0,
        "longitude": 0,
        "address": "string",
        "city": "string"
    }
    create_response = await client.post("/shop/create", json=shop_data)
    shop_id = create_response.json().get('_id')
    response = await client.delete(f"/shop/{shop_id}")
    assert response.status_code == 204
    get_response = await client.get(f"/shop/{shop_id}")
    assert get_response.status_code == 404
