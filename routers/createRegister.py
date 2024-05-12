from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
import re

router = APIRouter()


class register(BaseModel):
    name: str
    cpf: str
    address: str
    phone: constr(min_length=10, max_length=20)


@router.post("/create-register", status_code=201, response_model=register)
async def create_register(new_register: register):
    new_register.phone = re.sub(r'\D', '', new_register.phone)
    if new_register.phone[:2] is not "55":
        raise HTTPException(
            status_code=400,
            detail="Sorry but the Phone number should be from Brazil."
        )
    return new_register
