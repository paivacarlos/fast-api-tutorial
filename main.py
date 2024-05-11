from fastapi import FastAPI
from pydantic import BaseModel
from routers import createRegister

app = FastAPI()

app.include_router(createRegister.router)


@app.get("/health-check")
async def root():
    return {"message": "We are online! ;)"}
