from fastapi import APIRouter, status

from src.books.deps import BookServiceDep
from src.books.schemas import BookCreate, BookMessage, BookOut, BookUpdate

books_router = APIRouter()


@books_router.post(
    '/', response_model=BookOut, status_code=status.HTTP_201_CREATED
)
async def create(book_service: BookServiceDep, book_create: BookCreate):
    return await book_service.create(book_create)


@books_router.get('/', response_model=list[BookOut])
async def get_all(book_service: BookServiceDep):
    return await book_service.get_all()


@books_router.get('/{book_id}', response_model=BookOut)
async def get_one(book_service: BookServiceDep, book_id: int):
    return await book_service.get_one(book_id)


@books_router.patch('/{book_id}', response_model=BookOut)
async def update(
    book_service: BookServiceDep, book_id: int, book_update: BookUpdate
):
    return await book_service.update(book_id, book_update)


@books_router.delete('/{book_id}', response_model=BookMessage)
async def delete(book_service: BookServiceDep, book_id: int):
    return await book_service.delete(book_id)
