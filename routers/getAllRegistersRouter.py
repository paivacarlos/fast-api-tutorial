from fastapi import APIRouter
from services.getAllRegisterService import get_registers


router = APIRouter()


@router.get("/all-registers", status_code=200)
async def get_all_registers():
    return await get_registers()
