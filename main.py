from fastapi import FastAPI
from pydantic import BaseModel
from routers import createRegisterRouter
from routers import getAllRegistersRouter
from routers import getRegisterByIdRouter
from routers import updateRegisterRouter
from routers import deleteRegisterRouter

app = FastAPI()

app.include_router(createRegisterRouter.router)
app.include_router(getAllRegistersRouter.router)
app.include_router(getRegisterByIdRouter.router)
app.include_router(updateRegisterRouter.router)
app.include_router(deleteRegisterRouter.router)


@app.get("/health-check")
async def root():
    return {"message": "We are online! ;)"}
