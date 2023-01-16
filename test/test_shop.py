import json
import requests

ENDPOINT = "http://127.0.0.1:8000"


def test_can_call_endpoint():
	response = requests.get(ENDPOINT)
	assert response.status_code == 200


def test_can_create_shop():
	payload = new_shop_payload
	create_shop_response = create_shop(payload)
	assert create_shop_response.status_code == 201
	data = create_shop_response.json()
	print(data)

	shop_id = data['id']
	get_response = get_shop(shop_id)

	assert get_response.status_code == 200
	get_shop_data = get_response.json()
	print(get_shop_data)

	assert get_shop_data['name'] == payload['name']
	assert get_shop_data['address'] == payload['address']


def test_cat_update_shop():
	payload = new_shop_payload
	create_shop_response = create_shop(payload)
	assert create_shop_response == 201
	shop_id = create_shop_response.json()['id']

	new_payload = {
		"id": shop_id,
		"name": "Narodnyi",
		"latitude": 10,
		"longitude": payload['longitude'],
		"address": payload['address'],
		"city": payload['city']
	}
	update_shop_response = update_shop(new_payload)
	assert update_shop_response.status_code == 200

	get_shop_response = get_shop(shop_id)
	assert get_shop_response.status_code == 200
	get_shop_data = get_shop_response.json()
	print(get_shop_data)
	assert get_shop_data['name'] == new_payload['name']
	assert get_shop_data['latitude'] == new_payload['latitude']


def create_shop(payload):
	return requests.post(ENDPOINT + "/shop/create", json=json.dumps(payload))


def update_shop(payload):
	return requests.post(ENDPOINT + "/shop/update", json=json.dumps(payload))


def get_shop(shop_id):
	return requests.get(ENDPOINT + f"/shop/{shop_id}")


def new_shop_payload():
	data = {
		"id": "test shop",
		"name": "Narodnyi",
		"latitude": 12,
		"longitude": 1,
		"address": "Turusbekova",
		"city": "Bishkek"
	}
	return data
