from typing import Annotated

from fastapi import Depends

from src.auth.services import AuthService
from src.db.session import SessionDep


def get_auth_service(session: SessionDep) -> AuthService:
    return AuthService(session)


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
