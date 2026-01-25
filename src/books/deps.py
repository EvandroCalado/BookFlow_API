from typing import Annotated

from fastapi import Depends

from src.books.services import BookService
from src.db.session import SessionDep


def get_book_service(session: SessionDep):
    return BookService(session)


BookServiceDep = Annotated[BookService, Depends(get_book_service)]
