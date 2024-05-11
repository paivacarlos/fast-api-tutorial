from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class register(BaseModel):
    name: str
    cpf: str
    address: str
    phone: str


@router.post("/create-register")
async def create_register(new_register: register):
    return new_register
