from fastapi import APIRouter
from services.get_all_register_service import get_registers


router = APIRouter()


@router.get("/all-registers", status_code=200)
async def get_all_registers():
    return await get_registers()
