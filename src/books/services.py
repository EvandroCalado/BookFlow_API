from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.books.models import Book
from src.books.schemas import BookCreate, BookMessage, BookUpdate


class BookService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, book_create: BookCreate):
        new_book = Book(
            **book_create.model_dump(),
        )

        self.session.add(new_book)
        await self.session.commit()
        await self.session.refresh(new_book)

        return new_book

    async def get_all(self):
        stmt = select(Book)
        result = await self.session.execute(stmt)
        books = result.scalars().all()

        return books

    async def get_one(self, book_id: UUID):
        stmt = select(Book).where(Book.id == book_id)
        result = await self.session.execute(stmt)
        book = result.scalar_one_or_none()

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail='Book not found'
            )

        return book

    async def update(self, book_id: UUID, book_update: BookUpdate):
        book = await self.get_one(book_id)

        for key, value in book_update.model_dump(exclude_unset=True).items():
            setattr(book, key, value)

        await self.session.commit()
        await self.session.refresh(book)

        return book

    async def delete(self, book_id: UUID):
        book = await self.get_one(book_id)

        await self.session.delete(book)
        await self.session.commit()

        return BookMessage(message='Book deleted successfully')
