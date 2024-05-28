from pydantic import BaseModel, Field


class CreateUser(BaseModel):
    username: str = Field(..., max_length=15)
    password: str
