from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

from src.config import Config
from src.books.models import Book  # important: ensures model is registered

engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True
)

async def init_db():
    """Create database tables"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def test_connection():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 'Hello World'"))
        print(result.scalar())
