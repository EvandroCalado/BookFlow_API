from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import desc, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import col, select

from src.books.models import Book
from src.books.schemas import (
    BookCreate,
    BookMessage,
    BookUpdate,
    PaginatedBooksOut,
)


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

    async def get_all(self, page: int, limit: int):
        query = select(Book).order_by(desc(col(Book.created_at)))

        count_stmt = select(func.count(col(Book.id)))
        total = await self.session.scalar(count_stmt) or 0

        stmt = query.limit(limit).offset((page - 1) * limit)
        result = await self.session.execute(stmt)
        books = result.scalars().all()

        return PaginatedBooksOut(
            books=books,
            total=total,
            page=page,
            limit=limit,
        )

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
