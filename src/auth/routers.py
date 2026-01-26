from fastapi import APIRouter, status

from src.auth.deps import AuthServiceDep
from src.auth.schemas import UserCreate, UserOut

auth_router = APIRouter()


@auth_router.post(
    '/register', response_model=UserOut, status_code=status.HTTP_201_CREATED
)
async def register(service: AuthServiceDep, user_create: UserCreate):
    return await service.register(user_create)
