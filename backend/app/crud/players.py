from app.models import Player
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.players import PlayerCreateSchema, PlayerUpdateSchema


async def get_all_players(self, session: AsyncSession) -> list[Player]:
    try:
        stmt = select(Player).order_by(Player.id)
        result = await session.execute(stmt)
        players = result.scalars().all()
        return players
    except SQLAlchemyError:
        raise


async def get_player(self, session: AsyncSession, player_id: int) -> Player | None:
    try:
        stmt = select(Player).options(
            selectinload(Player.matches)
        ).filter_by(id=player_id)
        result = await session.execute(stmt)
        player = result.scalars().first()
        return player
    except SQLAlchemyError:
        raise


async def create_player(self, session: AsyncSession, player_create: PlayerCreateSchema) -> Player:
    try:
        new_player = Player(**player_create.model_dump())
        new_player.created_by = None
        new_player.created_at = datetime.now(timezone.utc)
        session.add(new_player)
        await session.flush()
        await session.commit()
        return new_player
    except SQLAlchemyError:
        await session.rollback()
        raise


async def update_player(self, session: AsyncSession, player: Player, player_update: PlayerUpdateSchema) -> Player:
    try:
        for key, value in player_update.model_dump(exclude_unset=True).items():
            setattr(player, key, value)
        player.updated_by = None
        player.last_update_at = datetime.now(timezone.utc)
        await session.commit()
        await session.refresh(player, attribute_names=["matches"])
        return player
    except SQLAlchemyError:
        await session.rollback()
        raise


async def delete_player(self, session: AsyncSession, player: Player) -> bool:
    try:
        await session.delete(player)
        await session.commit()
        return True
    except SQLAlchemyError:
        await session.rollback()
        return False
