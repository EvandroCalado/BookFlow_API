from datetime import timedelta

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from starlette.responses import JSONResponse

from src.auth.models import User
from src.auth.schemas import UserCreate, UserLogin, UserRegisterOut
from src.auth.utils import create_access_token, hash_password, verify_password
from src.db.config import settings


class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register(self, user_create: UserCreate) -> UserRegisterOut:
        stmt = select(User).where(User.email == user_create.email)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()

        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists',
            )

        new_user = User(
            username=user_create.username,
            email=user_create.email,
            password=hash_password(user_create.password),
        )

        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return UserRegisterOut(
            message='User registered successfully',
        )

    async def login(self, user_login: UserLogin):
        stmt = select(User).where(User.email == user_login.email)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()

        if not user or not verify_password(user_login.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Invalid email or password',
            )

        access_token = create_access_token(
            data={
                'user_id': str(user.id),
                'username': user.username,
                'email': user.email,
            }
        )

        refresh_token = create_access_token(
            data={
                'user_id': str(user.id),
                'username': user.username,
                'email': user.email,
            },
            refresh=True,
            expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        )

        return JSONResponse(
            content={
                'message': 'Login successful',
                'access_token': access_token,
                'refresh_token': refresh_token,
                'token_type': 'bearer',
            }
        )
