from fastapi import APIRouter
from .repository import ShopRepo
from .model import Shop, Response
from starlette import status


router = APIRouter()


@router.get("/shop/", status_code=status.HTTP_200_OK)
async def get_all():
    _shoplist = await ShopRepo.retrieve()
    return Response(code=200, status="Ok", message="Success retrieve all data", result=_shoplist).dict(exclude_none=True)


@router.post("/shop/create", status_code=status.HTTP_201_CREATED)
async def create(shop: Shop):
    _shoplist = await ShopRepo.insert(shop)
    return Response(code=200, status="Ok", message="Success save data", result=_shoplist).dict(exclude_none=True)


@router.get("/shop/{id}", status_code=status.HTTP_200_OK)
async def get_id(id: str):
	_shop = await ShopRepo.retrieve_id(id)
	return Response(code=200, status="Ok", message="Success retrieve data", result=_shop).dict(exclude_none=True)


@router.post("/shop/update")
async def update(shop: Shop):
	await ShopRepo.update(shop.id, shop)
	return Response(code=200, status="Ok", message="Success update data").dict(exclude_none=True)


@router.delete("/shop/{id}")
async def delete(id: str):
	await ShopRepo.delete(id)
	return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)
