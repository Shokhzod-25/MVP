from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)
from app.core.config import settings
from app.core.models.base import Base


class DataBase:
    def __init__(self):
        self.engine = create_async_engine(url=settings.DATABASE_URL, echo=False)
        self.session_f = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False
        )

    async def session_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_f() as session:
            yield session

    async def init_database(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


db = DataBase()
