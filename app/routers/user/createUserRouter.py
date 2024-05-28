from fastapi import APIRouter
from app.models.createUserModels import CreateUser


router = APIRouter()


@router.post("/user", status_code=201)
async def create_user(user: CreateUser):
    return user
