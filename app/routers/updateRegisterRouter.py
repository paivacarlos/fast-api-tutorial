from fastapi import APIRouter, HTTPException
from app.services.updateRegisterService import update_register
from app.services.getRegisterByIdService import get_register
from app.models.registerModels import Register

router = APIRouter()


@router.put("/update-register/{register_id}", status_code=200)
async def update_register_id(register_id: int, update_data: Register):
    # Verificar se o registro existe
    existing_register = await get_register(register_id)
    if existing_register is None:
        raise HTTPException(status_code=404, detail="Register not found")

    # Atualizar o registro
    await update_register(register_id, update_data)

    return {"message": "Register updated successfully"}
