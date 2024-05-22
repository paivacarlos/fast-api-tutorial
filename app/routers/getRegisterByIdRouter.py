from fastapi import APIRouter, HTTPException
from app.services.getRegisterByIdService import get_register

router = APIRouter()


@router.get("/register/{register_id}", status_code=200)
async def get_register_by_id(register_id: int):
    register = await get_register(register_id)
    if register is not None:
        return register
    else:
        raise HTTPException(
            status_code=400,
            detail="Sorry id not found!"
        )
