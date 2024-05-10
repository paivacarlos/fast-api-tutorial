from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/health-check")
async def root():
    return {"message": "We are online! ;)"}


class register(BaseModel):
    name: str
    cpf: str
    address: str
    phone: str


@app.post("/create-register")
async def create_register(register: register):
    return register
