from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from fastapi import Depends
from typing import Annotated, AsyncIterator
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logger = logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://{}:{}@{}/{}".format(
    os.environ.get('DB_USER', ''),
    os.environ.get('DB_PASS', ''),
    os.environ.get('DB_HOST', ''),
    os.environ.get('DB_DATABASE', '')
)

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Base = declarative_base()

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine, 
    autoflush=False,
    future=True,
    expire_on_commit=False
)


async def get_session() -> AsyncIterator[async_sessionmaker]:
    try:
        yield AsyncSessionLocal
    except SQLAlchemyError as e:
        logger.exception(e)
