from fastapi import APIRouter, HTTPException
from services.deleteRegisterService import delete_register_by_id

router = APIRouter()


@router.delete("/delete-register/{register_id}", status_code=200)
async def delete_register(register_id: int):
    result = await delete_register_by_id(register_id)
    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["message"])
    return {"message": result["message"]}
