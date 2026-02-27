from fastapi import Depends, APIRouter, HTTPException, status
from app.schemas.players import PlayerSlimSchema, PlayerSchema, PlayerCreateSchema, PlayerUpdateSchema
from app.database.database import get_session
from app.services.players import PlayerService

router = APIRouter(prefix='/players', tags=['players'])


@router.get('/', response_model=list[PlayerSlimSchema])
async def get_players(session=Depends(get_session)) -> PlayerSlimSchema:
    service = PlayerService(session)
    players = await service.get_all_players()
    return players


@router.get('/{id}', response_model=PlayerSchema)
async def get_player(id: int, session=Depends(get_session)):
    service = PlayerService(session)
    player = await service.get_player(id)
    if player is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player with id {id} not found."
        )
    return player


@router.post('/', response_model=PlayerSchema)
async def create_player(player_create: PlayerCreateSchema, session=Depends(get_session)):
    service = PlayerService(session)
    player = await service.create_player(player_create)
    if player is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Player could not be created."
        )
    return player


@router.put('/{id}', response_model=PlayerSchema)
async def update_player(id: int, player_update: PlayerUpdateSchema, session=Depends(get_session)):
    service = PlayerService(session)
    player = await service.update_player(id, player_update)
    if player is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player with id {id} not found."
        )
    return player


@router.delete('/{id}', status_code=204)
async def delete_player(id: int, session=Depends(get_session)):
    service = PlayerService(session)
    deleted = await service.delete_player(id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player with id {id} not found."
        )
    return None
