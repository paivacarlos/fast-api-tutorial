from fastapi import APIRouter


router = APIRouter()


@router.post("/user", status_code=201)
async def create_user():
    return {"message": "This api is building..."}
