from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


class Config:
    DB_URL = "postgresql+asyncpg://postgres:fE512@localhost:5432/contacts"


config = Config

