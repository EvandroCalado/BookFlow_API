from fastapi import HTTPException, status

from src.books.models import Book
from src.books.schemas import BookCreate, BookMessage, BookUpdate


class BookService:
    def __init__(self, books: list[Book]):
        self.books = books

    async def create(self, book_create: BookCreate):
        new_book = Book(
            id=len(self.books) + 1,
            **book_create.model_dump(),
        )

        self.books.append(new_book)

        return new_book

    async def get_all(self):
        return self.books

    async def get_one(self, book_id: int):
        for book in self.books:
            if book.id == book_id:
                return book

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Book not found'
        )

    async def update(self, book_id: int, book_update: BookUpdate):
        book = await self.get_one(book_id)

        for key, value in book_update.model_dump(exclude_unset=True).items():
            setattr(book, key, value)

        return book

    async def delete(self, book_id: int):
        book = await self.get_one(book_id)

        if book:
            self.books.remove(book)

        return BookMessage(message='Book deleted successfully')
