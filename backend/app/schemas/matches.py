from pydantic import BaseModel
from app.schemas import MatchBaseSchema
from typing import Optional
from datetime import datetime


class MatchSchema(MatchBaseSchema):
    id: int
    is_active: bool


class MatchSlimSchema(MatchBaseSchema):
    id: int
    is_active: bool


class MatchCreateSchema(MatchBaseSchema):
    players: list[dict] = None


class MatchUpdateSchema(BaseModel):
    date: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    teamA_name: Optional[str] = None
    teamB_name: Optional[str] = None
    teamA_score: Optional[int] = None
    teamB_score: Optional[int] = None
    location_id: Optional[int] = None
    mvp_id: Optional[int] = None
    players: list[dict] = None
