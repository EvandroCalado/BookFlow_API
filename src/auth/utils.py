from datetime import datetime, timedelta
from typing import Any
from uuid import uuid4

import jwt
from fastapi import HTTPException, status
from passlib.context import CryptContext

from src.db.config import settings

pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_access_token(
    data: dict,
    refresh: bool = False,
    expires_delta: timedelta = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    ),
) -> str:
    payload: dict[str, Any] = {}

    payload['user'] = data
    payload['exp'] = datetime.now() + expires_delta
    payload['jti'] = str(uuid4())
    payload['refresh'] = refresh

    token = jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )

    return token


def decode_token(token: str) -> dict[str, Any]:
    try:
        payload = jwt.decode(
            jwt=token,
            key=settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Token expired'
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token'
        )
