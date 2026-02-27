from app.models import Player
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.players import PlayerCreateSchema, PlayerUpdateSchema


async def get_all_players(self, session: AsyncSession) -> list[Player]:
    async with session() as session:
        stmt = select(Player).order_by(Player.id)
        result = await session.execute(stmt)
        players = result.scalars().all()
        return players


async def get_player(self, session: AsyncSession, player_id: int) -> Player | None:
    async with session() as session:
        stmt = select(Player).options(
            selectinload(Player.matches)
        ).filter_by(id=player_id)
        result = await session.execute(stmt)
        player = result.scalars().first()
        return player


async def create_player(self, session: AsyncSession, player_create: PlayerCreateSchema) -> Player | None:
    async with session() as session:
        new_player = Player(**player_create.dict())
        new_player.created_by = None
        new_player.created_at = datetime.now(timezone.utc)
        session.add(new_player)
        await session.commit()
        stmt = select(Player).options(
            selectinload(Player.matches)
        ).filter_by(id=new_player.id)
        result = await session.execute(stmt)
        new_player = result.scalars().first()
        return new_player


async def update_player(self, session: AsyncSession, player_id: int, player_update: PlayerUpdateSchema) -> Player | None:
    async with session() as session:
        stmt = select(Player).filter_by(id=player_id)
        result = await session.execute(stmt)
        player = result.scalars().first()
        if player is None:
            return None
        for key, value in player_update.dict(exclude_unset=True).items():
            setattr(player, key, value)
        player.updated_by = None
        player.last_update_at = datetime.now(timezone.utc)
        session.add(player)
        await session.commit()
        stmt = select(Player).options(
            selectinload(Player.matches)
        ).filter_by(id=player.id)
        result = await session.execute(stmt)
        player = result.scalars().first()
        return player


async def delete_player(self, session: AsyncSession, player_id: int) -> bool:
    async with session() as session:
        stmt = select(Player).filter_by(id=player_id)
        result = await session.execute(stmt)
        player = result.scalars().first()
        if player is None:
            return False
        await session.delete(player)
        await session.commit()
        return True
