from fastapi import FastAPI
from geo.routes import router

app = FastAPI()


@app.get("/")
async def Home():
	return "Welcome"

app.include_router(router)
