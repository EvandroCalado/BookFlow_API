from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    published_date: date | None = None
    page_count: int | None = None
    language: str | None = None


class BookOut(BookBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PaginatedBooksOut(BaseModel):
    books: list[BookOut]
    total: int
    page: int
    limit: int


class PaginationParams(BaseModel):
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=10, ge=1, le=100)


class BookMessage(BaseModel):
    message: str
