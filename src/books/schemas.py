from uuid import UUID

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    published_date: str | None = None
    page_count: int | None = None
    language: str | None = None


class BookOut(BookBase):
    id: UUID


class BookMessage(BaseModel):
    message: str
