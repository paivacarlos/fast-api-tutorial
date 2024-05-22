from fastapi import APIRouter
from app.models.registerModels import Register
from app.services.createRegisterService import create_register


router = APIRouter()


@router.post("/create-register", status_code=201)
async def create_new_register(new_register: Register):
    return await create_register(new_register)
