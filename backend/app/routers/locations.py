from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from app.database.models import Location
from app.database.database import get_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

router = APIRouter(prefix='/locations', tags=['locations'])

@router.get('/')
async def get_locations(session = Depends(get_session)) -> JSONResponse:
	async with session() as session:
		try:
			stmt = select(Location).order_by(Location.id)
			result = await session.execute(stmt)
			locations = result.scalars().all()
			return jsonable_encoder(locations)
		except Exception as ex:
			return JSONResponse({'ok': False, 'error': str(ex)}, status_code=500)

@router.get('/{id}')
async def get_location(id: int, session= Depends(get_session)) -> JSONResponse:
	try:
		stmt = select(Location).filter_by(id=id)
		result = await session.execute(stmt)
		location = result.scalars().one()
		return jsonable_encoder(location)
	except NoResultFound as ex:
		return JSONResponse({'ok': False, 'error': str(ex)}, status_code=404)    
