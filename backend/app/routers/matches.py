from app.utils.exceptions import MatchCannotBeDeletedException, MatchNotFoundException
from fastapi import Depends, APIRouter, HTTPException, status, Response
from app.schemas.matches import MatchCreateSchema, MatchUpdateSchema, MatchSchema, MatchSlimSchema
from app.database.database import get_session
from app.services.matches import MatchService

router = APIRouter(prefix='/matches', tags=['matches'])


@router.get('/', response_model=list[MatchSlimSchema])
async def get_matches(location: int=0, pichichi: int=0, mvp: int=0, session=Depends(get_session)):
    service = MatchService(session)
    matches = await service.get_all_matches()
    return matches


@router.get('/{id}', response_model=MatchSchema)
async def get_match(id: int, session=Depends(get_session)):
    service = MatchService(session)
    match = await service.get_match(id)
    if match is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Match with id {id} not found."
        )
    return match


@router.post('/', response_model=MatchSchema)
async def create_match(match_create: MatchCreateSchema, session=Depends(get_session)):
    service = MatchService(session)
    match = await service.create_match(match_create)
    if match is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Match could not be created."
        )
    return match


@router.put('/{id}', response_model=MatchSchema)
async def update_match(id: int, match_update: MatchUpdateSchema, session=Depends(get_session)):
    service = MatchService(session)
    match = await service.update_match(id, match_update)
    if match is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Match with id {id} not found."
        )
    return match


@router.delete('/{id}', status_code=204)
async def delete_match(id: int, session=Depends(get_session)):
    service = MatchService(session)
    try:
        deleted = await service.delete_match(id)
    except MatchNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except MatchCannotBeDeletedException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
