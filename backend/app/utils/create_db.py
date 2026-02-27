from app.database.database import async_engine
import app.models as models
from app.database.database import Base
import asyncio


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(async_main())