from app.models import Match
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from datetime import datetime, timezone
from app.schemas.matches import MatchCreateSchema, MatchUpdateSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError


async def get_all_matches(self, session: AsyncSession) -> list[Match]:
    try:
        stmt = select(Match).order_by(Match.id)
        result = await session.execute(stmt)
        matches = result.scalars().all()
        return matches
    except SQLAlchemyError:
        raise


async def get_match(self, session: AsyncSession, match_id: int) -> Match | None:
    try:
        stmt = select(Match).options(
            selectinload(Match.player_associations)
        ).filter_by(id=match_id)
        result = await session.execute(stmt)
        match = result.scalars().first()
        return match
    except SQLAlchemyError:
        raise


async def create_match(self, session: AsyncSession, match_create: MatchCreateSchema) -> Match:
    try:
        new_match = Match(**match_create.model_dump())
        new_match.created_by = None
        new_match.created_at = datetime.now(timezone.utc)
        session.add(new_match)
        await session.flush()
        await session.commit()
        await session.refresh(new_match, attribute_names=["player_associations"])
        return new_match
    except SQLAlchemyError:
        await session.rollback()
        raise


async def update_match(self, session: AsyncSession, match: Match, match_update: MatchUpdateSchema) -> Match:
    try:
        for key, value in match_update.model_dump(exclude_unset=True).items():
            setattr(match, key, value)
        match.updated_by = None
        match.last_update_at = datetime.now(timezone.utc)
        await session.commit()
        await session.refresh(match, attribute_names=["player_associations"])
        return match
    except SQLAlchemyError:
        await session.rollback()
        raise


async def delete_match(self, session: AsyncSession, match: Match) -> bool:
    try:
        await session.delete(match)
        await session.commit()
        return True
    except SQLAlchemyError as e:
        await session.rollback()
        return False
