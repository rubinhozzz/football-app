from app.crud import players as crud
from app.models import Player
from app.schemas.players import PlayerCreateSchema, PlayerUpdateSchema
from sqlalchemy.ext.asyncio import AsyncSession


class PlayerService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_players(self) -> list[Player]:
        return await crud.get_all_players(self, self.session)

    async def get_player(self, player_id: int) -> Player | None:
        return await crud.get_player(self, self.session, player_id)

    async def create_player(self, player_create: PlayerCreateSchema) -> Player | None:
        return await crud.create_player(self, self.session, player_create)

    async def update_player(self, player_id: int, player_update: PlayerUpdateSchema) -> Player | None:
        return await crud.update_player(self, self.session, player_id, player_update)

    async def delete_player(self, player_id: int) -> bool:
        return await crud.delete_player(self, self.session, player_id)
