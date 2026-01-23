from fastapi import FastAPI

from src.books.routers import books_router

app = FastAPI(
    title='BookFlow API',
    description='API for managing books',
    version='1.0.0',
)

app.include_router(books_router, prefix='/books', tags=['Books'])
