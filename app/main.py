from fastapi import FastAPI
from app.routers import createRegisterRouter, getRegisterByIdRouter, deleteRegisterRouter, updateRegisterRouter
from app.routers import getAllRegistersRouter
from app.routers.user import createUserRouter

app = FastAPI()

app.include_router(createRegisterRouter.router)
app.include_router(getAllRegistersRouter.router)
app.include_router(getRegisterByIdRouter.router)
app.include_router(updateRegisterRouter.router)
app.include_router(deleteRegisterRouter.router)
app.include_router(createUserRouter.router)


@app.get("/health-check")
async def root():
    return {"message": "We are online! ;)"}
