from fastapi import APIRouter

router = APIRouter()


@router.put("/update-register/{register_id}", status_code=200)
async def update_register(register_id: int):
    # return await create_register(new_register)
    return {"message": "API is building."}
