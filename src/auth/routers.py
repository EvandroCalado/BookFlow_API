from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from src.auth.deps import AuthServiceDep, CurrentUserDep, OAuth2FormDep
from src.auth.schemas import UserCreate, UserOut, UserRegisterOut

auth_router = APIRouter()


@auth_router.post(
    '/register',
    response_model=UserRegisterOut,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    service: AuthServiceDep, user_create: UserCreate
) -> UserRegisterOut:
    return await service.register(user_create)


@auth_router.post('/login')
async def login(
    service: AuthServiceDep, form_data: OAuth2FormDep
) -> JSONResponse:
    return await service.login(form_data)


@auth_router.get('/me', response_model=UserOut)
async def me(user: CurrentUserDep):
    return user
