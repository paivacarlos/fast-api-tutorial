from fastapi import APIRouter

router = APIRouter()


@router.delete("/delete-register/{register_id}", status_code=200)
async def delete_register_id():
    return {"message": "Sorry. This API is building."}
