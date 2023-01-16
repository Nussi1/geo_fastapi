from typing import TypeVar, Optional
from pydantic import BaseModel


T = TypeVar('T')


class Shop(BaseModel):
	id: str = None
	name: str
	latitude: int
	longitude: int
	address: str
	city: str


class Response(BaseModel):
	code: str
	status: str
	message: str
	result: Optional[T] = None
