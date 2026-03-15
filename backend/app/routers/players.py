from app.utils.exceptions import PlayerCannotBeDeletedException, PlayerNotFoundException
from fastapi import Depends, APIRouter, HTTPException, status, Response
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
    try:
        player = await service.get_player(id)
    except PlayerNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )   
    return player


@router.post('/', response_model=PlayerSchema)
async def create_player(player_create: PlayerCreateSchema, session=Depends(get_session)):
    service = PlayerService(session)
    player = await service.create_player(player_create)
    return player


@router.put('/{id}', response_model=PlayerSchema)
async def update_player(id: int, player_update: PlayerUpdateSchema, session=Depends(get_session)):
    service = PlayerService(session)
    player = await service.update_player(id, player_update)
    return player


@router.delete('/{id}', status_code=204)
async def delete_player(id: int, session=Depends(get_session)):
    service = PlayerService(session)
    try:
        await service.delete_player(id)
    except PlayerNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except PlayerCannotBeDeletedException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
