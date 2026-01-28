from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.models import User
from src.auth.services import AuthService
from src.auth.utils import get_current_user
from src.db.session import SessionDep


def get_auth_service(session: SessionDep) -> AuthService:
    return AuthService(session)


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
CurrentUserDep = Annotated[User, Depends(get_current_user)]
OAuth2FormDep = Annotated[OAuth2PasswordRequestForm, Depends()]
