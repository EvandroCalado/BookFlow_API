from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.auth.models import User
from src.auth.schemas import UserCreate
from src.auth.utils import hash_password


class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register(self, user_create: UserCreate):
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

        return new_user
