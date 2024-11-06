from fastapi import Request, APIRouter

api_router = APIRouter(prefix="/v1", tags=["api"])

@api_router.get("")
async def home(req: Request):
    return "fastapi"