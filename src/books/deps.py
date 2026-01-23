from typing import Annotated

from fastapi import Depends

from src.books.books_data import books as books_data
from src.books.models import Book
from src.books.services import BookService

books_db: list[Book] = [Book(**book) for book in books_data]


def get_book_service():
    return BookService(books_db)


BookServiceDep = Annotated[BookService, Depends(get_book_service)]
