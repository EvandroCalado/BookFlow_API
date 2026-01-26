from fastapi import APIRouter, status

from src.auth.deps import AuthServiceDep
from src.auth.schemas import UserCreate, UserLogin, UserRegisterOut

auth_router = APIRouter()


@auth_router.post(
    '/register',
    response_model=UserRegisterOut,
    status_code=status.HTTP_201_CREATED,
)
async def register(service: AuthServiceDep, user_create: UserCreate):
    return await service.register(user_create)


@auth_router.post('/login')
async def login(service: AuthServiceDep, user_login: UserLogin):
    return await service.login(user_login)
