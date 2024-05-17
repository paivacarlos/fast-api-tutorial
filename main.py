from fastapi import FastAPI
from pydantic import BaseModel
from routers import createRegister
from routers import getAllRegisters
from routers import getRegisterById
from routers import updateRegister
from routers import deleteRegister

app = FastAPI()

app.include_router(createRegister.router)
app.include_router(getAllRegisters.router)
app.include_router(getRegisterById.router)
app.include_router(updateRegister.router)
app.include_router(deleteRegister.router)


@app.get("/health-check")
async def root():
    return {"message": "We are online! ;)"}
