from .model import Shop
from .config import database
import uuid


class ShopRepo():

	@staticmethod
	async def retrieve():
		_shop = []
		collection = database.get_collection('shop').find()
		async for shop in collection:
			_shop.append(shop)
		return _shop

	@staticmethod
	async def insert(shop: Shop):
		id = str(uuid.uuid4())
		_shop = {
			"_id": id,
			"name": shop.name,
			"latitude": shop.latitude,
			"longitude": shop.longitude,
			"address": shop.address,
			"city": shop.city,
		}
		await database.get_collection('shop').insert_one(_shop)

	@staticmethod
	async def update(id: str, shop: Shop):
		_shop = await database.get_collection('shop').find_one({"_id": id})
		_shop['name'] = shop.name
		_shop['latitude'] = shop.latitude
		_shop['longitude'] = shop.longitude
		_shop['address'] = shop.address
		_shop['city'] = shop.city
		await database.get_collection('shop').update_one({"_id": id}, {"$set": _shop})

	@staticmethod
	async def retrieve_id(id: str):
		return await database.get_collection('shop').find_one({"_id": id})

	@staticmethod
	async def delete(id: str):
		await database.get_collection('shop').delete_one({"_id": id})



