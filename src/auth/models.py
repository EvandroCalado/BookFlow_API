from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy.dialects import postgresql as pg
from sqlmodel import Column, Field, SQLModel


class User(SQLModel, table=True):
    id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            unique=True,
            nullable=False,
            default=uuid4,
        ),
    )
    username: str
    email: str = Field(
        sa_column=Column(
            pg.VARCHAR,
            unique=True,
            nullable=False,
        )
    )
    password: str
    is_verified: bool = Field(
        sa_column=Column(
            pg.BOOLEAN,
            default=False,
        )
    )
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
            onupdate=datetime.now,
        )
    )

    def __repr__(self) -> str:
        return f'<User {self.username}>'
