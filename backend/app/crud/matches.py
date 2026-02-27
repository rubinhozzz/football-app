from app.models import Match
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from datetime import datetime, timezone
from app.schemas.matches import MatchCreateSchema, MatchUpdateSchema
from sqlalchemy.ext.asyncio import AsyncSession


async def get_all_matches(self, session: AsyncSession) -> list[Match]:
    async with session() as session:
        stmt = select(Match).order_by(Match.id)
        result = await session.execute(stmt)
        matches = result.scalars().all()
        return matches


async def get_match(self, session: AsyncSession, match_id: int) -> Match | None:
    async with session() as session:
        stmt = select(Match).options(
            selectinload(Match.player_associations)
        ).filter_by(id=match_id)
        result = await session.execute(stmt)
        match = result.scalars().first()
        return match


async def create_match(self, session: AsyncSession, match_create: MatchCreateSchema) -> Match | None:
    async with session() as session:
        new_match = Match(**match_create.dict())
        new_match.created_by = None
        new_match.created_at = datetime.now(timezone.utc)
        session.add(new_match)
        await session.commit()
        stmt = select(Match).options(
            selectinload(Match.player_associations)
        ).filter_by(id=new_match.id)
        result = await session.execute(stmt)
        new_match = result.scalars().first()
        return new_match


async def update_match(self, session: AsyncSession, match_id: int, match_update: MatchUpdateSchema) -> Match | None:
    async with session() as session:
        stmt = select(Match).filter_by(id=match_id)
        result = await session.execute(stmt)
        match = result.scalars().first()
        if match is None:
            return None
        for key, value in match_update.dict(exclude_unset=True).items():
            setattr(match, key, value)
        session.add(match)
        await session.commit()
        stmt = select(Match).options(
            selectinload(Match.player_associations)
        ).filter_by(id=match.id)
        result = await session.execute(stmt)
        match = result.scalars().first()
        return match


async def delete_match(self, session: AsyncSession, match_id: int) -> bool:
    async with session() as session:
        stmt = select(Match).filter_by(id=match_id)
        result = await session.execute(stmt)
        match = result.scalars().first()
        if match is None:
            return False
        await session.delete(match)
        await session.commit()
        return True
