from app.models import Match
from app.crud import matches as crud
from app.schemas.matches import MatchCreateSchema, MatchUpdateSchema
from sqlalchemy.ext.asyncio import AsyncSession


class MatchService:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_matches(self) -> list[Match]:
        return await crud.get_all_matches(self, self.session)

    async def get_match(self, id: int) -> Match | None:
        return await crud.get_match(self, self.session, id)

    async def create_match(self, match_create: MatchCreateSchema) -> Match | None:
        return await crud.create_match(self, self.session, match_create)   

    async def update_match(self, id: int, match_update: MatchUpdateSchema) -> Match | None:
        return await crud.update_match(self, self.session, id, match_update)

    async def delete_match(self, id: int) -> bool:
        return await crud.delete_match(self, self.session, id)
