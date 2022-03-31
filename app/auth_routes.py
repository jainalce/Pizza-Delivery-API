from fastapi import APIRouter

auth_router=APIRouter(prefix="/login")

@auth_router.get("/")
async def hello():
    return {"message": "hello world"}