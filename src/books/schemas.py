from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    publisher: str
    publisher_date: str
    pages: int
    language: str


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    publisher_date: str | None = None
    pages: int | None = None
    language: str | None = None


class BookOut(BookBase):
    id: int


class BookMessage(BaseModel):
    message: str
