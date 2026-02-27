import asyncio
from app.database.database import async_engine as engine, Base
import app.models  # Ensure all models are imported so that they are registered with Base


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(async_main())
