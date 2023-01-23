from fastapi import FastAPI
from geo import routes

app = FastAPI()


@app.get("/")
async def Home():
	return "Welcome"

app.include_router(routes.router)
