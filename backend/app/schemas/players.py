from pydantic import BaseModel
from app.schemas import PlayerBaseSchema
from app.schemas.matches import MatchSlimSchema
from typing import Optional


class PlayerSchema(PlayerBaseSchema):
    id: int
    is_active: bool
    matches: Optional[list[MatchSlimSchema]]


class PlayerSlimSchema(PlayerBaseSchema):
    id: int
    is_active: bool


class PlayerCreateSchema(PlayerBaseSchema):
    pass


class PlayerUpdateSchema(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    country_code: Optional[str] = None
    is_active: Optional[bool] = None
